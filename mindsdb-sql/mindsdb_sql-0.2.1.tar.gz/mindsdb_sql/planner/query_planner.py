import copy
from collections import defaultdict
from mindsdb_sql.exceptions import PlanningException
from mindsdb_sql.parser.ast import (Select, Identifier, Join, Star, BinaryOperation, Constant, OrderBy,
                                    BetweenOperation, Union, NullConstant, CreateTable)

from mindsdb_sql.parser.dialects.mindsdb.latest import Latest
from mindsdb_sql.planner.steps import (FetchDataframeStep, ProjectStep, JoinStep, ApplyPredictorStep,
                                       ApplyPredictorRowStep, FilterStep, GroupByStep, LimitOffsetStep, OrderByStep,
                                       UnionStep, MapReduceStep, MultipleSteps, ApplyTimeseriesPredictorStep,
                                       GetPredictorColumns, SaveToTable)
from mindsdb_sql.planner.ts_utils import (validate_ts_where_condition, find_time_filter, replace_time_filter,
                                          find_and_remove_time_filter)
from mindsdb_sql.planner.utils import (get_integration_path_from_identifier,
                                       get_predictor_namespace_and_name_from_identifier,
                                       disambiguate_integration_column_identifier,
                                       disambiguate_predictor_column_identifier, recursively_disambiguate_identifiers,
                                       get_deepest_select,
                                       recursively_extract_column_values,
                                       recursively_check_join_identifiers_for_ambiguity,
                                       query_traversal)
from mindsdb_sql.planner.query_plan import QueryPlan
from .query_prepare import PreparedStatementPlanner



class QueryPlanner():

    def __init__(self,
                 query=None,
                 integrations=None,
                 predictor_namespace=None,
                 predictor_metadata=None,
                 default_namespace=None):
        self.query = query
        self.plan = QueryPlan()

        self.integrations = [int.lower() for int in integrations] if integrations else []
        self.predictor_namespace = predictor_namespace.lower() if predictor_namespace else 'mindsdb'
        self.predictor_metadata = predictor_metadata or defaultdict(dict)
        self.default_namespace = default_namespace

        self.statement = None

    def is_predictor(self, identifier):
        parts = identifier.parts
        if parts[0].lower() == self.predictor_namespace:
            return True
        elif len(parts) == 1 and self.default_namespace == self.predictor_namespace:
            return True
        return False

    # not used
    # def is_integration_table(self, identifier):
    #     parts = identifier.parts
    #     if parts[0].lower() in self.integrations:
    #         return True
    #     elif len(parts) == 1 and self.default_namespace in self.integrations:
    #         return True
    #     return False

    def get_integration_path_from_identifier_or_error(self, identifier, recurse=True):
        try:
            integration_name, table = get_integration_path_from_identifier(identifier)
            if not integration_name.lower() in self.integrations:
                raise PlanningException(f'Unknown integration {integration_name} for table {str(identifier)}. Available integrations: {", ".join(self.integrations)}')
        except PlanningException:
            if not recurse or not self.default_namespace:
                raise
            else:
                new_identifier = copy.deepcopy(identifier)
                new_identifier.parts = [self.default_namespace, *identifier.parts]
                return self.get_integration_path_from_identifier_or_error(new_identifier, recurse=False)
        return integration_name, table

    def get_integration_select_step(self, select):
        integration_name, table = self.get_integration_path_from_identifier_or_error(select.from_table)

        fetch_df_select = copy.deepcopy(select)
        recursively_disambiguate_identifiers(fetch_df_select, integration_name, table)

        return FetchDataframeStep(integration=integration_name, query=fetch_df_select)

    def plan_integration_select(self, select):
        """Plan for a select query that can be fully executed in an integration"""

        return self.plan.add_step(self.get_integration_select_step(select))

    def plan_integration_nested_select(self, select):
        fetch_df_select = copy.deepcopy(select)
        deepest_select = get_deepest_select(fetch_df_select)
        integration_name, table = self.get_integration_path_from_identifier_or_error(deepest_select.from_table)
        recursively_disambiguate_identifiers(deepest_select, integration_name, table)
        return self.plan.add_step(FetchDataframeStep(integration=integration_name, query=fetch_df_select))

    def plan_select_from_predictor(self, select):
        predictor_namespace, predictor = get_predictor_namespace_and_name_from_identifier(select.from_table, self.default_namespace)

        if select.where == BinaryOperation('=', args=[Constant(1), Constant(0)]):
            # Hardcoded mysql way of getting predictor columns
            predictor_step = self.plan.add_step(
                GetPredictorColumns(namespace=predictor_namespace,
                                      predictor=predictor)
            )
        else:
            new_query_targets = []
            for target in select.targets:
                if isinstance(target, Identifier):
                    new_query_targets.append(
                        disambiguate_predictor_column_identifier(target, predictor))
                elif type(target) in (Star, Constant):
                    new_query_targets.append(target)
                else:
                    raise PlanningException(f'Unknown select target {type(target)}')

            if select.group_by or select.having:
                raise PlanningException(f'Unsupported operation when querying predictor. Only WHERE is allowed and required.')

            row_dict = {}
            where_clause = select.where
            if not where_clause:
                raise PlanningException(f'WHERE clause required when selecting from predictor')

            recursively_extract_column_values(where_clause, row_dict, predictor)

            predictor_step = self.plan.add_step(
                ApplyPredictorRowStep(namespace=predictor_namespace,
                                                predictor=predictor,
                                                row_dict=row_dict)
            )
        project_step = self.plan_project(select, predictor_step.result)
        return predictor_step, project_step

    def plan_predictor(self, query, table, predictor_namespace, predictor):
        integration_select_step = self.plan_integration_select(
            Select(targets=[Star()],
                                            from_table=table,
                                            where=query.where,
                                            group_by=query.group_by,
                                            having=query.having,
                                            order_by=query.order_by,
                                            limit=query.limit,
                                            offset=query.offset,
                                            )
        )
        predictor_step = self.plan.add_step(ApplyPredictorStep(namespace=predictor_namespace,
                                         dataframe=integration_select_step.result,
                                         predictor=predictor))

        return {
            'predictor': predictor_step,
            'data': integration_select_step
        }

    def plan_fetch_timeseries_partitions(self, query, table, predictor_group_by_names):
        targets = [
            Identifier(column)
            for column in predictor_group_by_names
        ]

        query = Select(
            distinct=True,
            targets=targets,
            from_table=table,
            where=query.where,
        )
        select_step = self.plan_integration_select(query)
        return select_step

    def plan_timeseries_predictor(self, query, table, predictor_namespace, predictor):
        predictor_name = predictor.to_string(alias=False)

        predictor_time_column_name = self.predictor_metadata[predictor_name]['order_by_column']
        predictor_group_by_names = self.predictor_metadata[predictor_name]['group_by_columns']
        if predictor_group_by_names is None:
            predictor_group_by_names = []
        predictor_window = self.predictor_metadata[predictor_name]['window']

        if query.order_by:
            raise PlanningException(
                f'Can\'t provide ORDER BY to time series predictor, it will be taken from predictor settings. Found: {query.order_by}')

        saved_limit = query.limit

        if query.group_by or query.having or query.offset:
            raise PlanningException(f'Unsupported query to timeseries predictor: {str(query)}')

        allowed_columns = [predictor_time_column_name.lower()]
        if len(predictor_group_by_names) > 0:
            allowed_columns += [i.lower() for i in predictor_group_by_names]
        validate_ts_where_condition(query.where, allowed_columns=allowed_columns)

        time_filter = find_time_filter(query.where, time_column_name=predictor_time_column_name)

        order_by = [OrderBy(Identifier(parts=[predictor_time_column_name]), direction='DESC')]

        preparation_where = copy.deepcopy(query.where)

        # add {order_by_field} is not null
        def add_order_not_null(condition):
            order_field_not_null = BinaryOperation(op='is not', args=[
                Identifier(parts=[predictor_time_column_name]),
                NullConstant()
            ])
            if condition is not None:
                condition = BinaryOperation(op='and', args=[
                    condition,
                    order_field_not_null
                ])
            else:
                condition = order_field_not_null
            return condition

        preparation_where2 = copy.deepcopy(preparation_where)
        preparation_where = add_order_not_null(preparation_where)

        # Obtain integration selects
        if isinstance(time_filter, BetweenOperation):
            between_from = time_filter.args[1]
            preparation_time_filter = BinaryOperation('<', args=[Identifier(predictor_time_column_name), between_from])
            preparation_where2 = replace_time_filter(preparation_where2, time_filter, preparation_time_filter)
            integration_select_1 = Select(targets=[Star()],
                                        from_table=table,
                                        where=add_order_not_null(preparation_where2),
                                        order_by=order_by,
                                        limit=Constant(predictor_window))

            integration_select_2 = Select(targets=[Star()],
                                          from_table=table,
                                          where=preparation_where,
                                          order_by=order_by)

            integration_selects = [integration_select_1, integration_select_2]
        elif isinstance(time_filter, BinaryOperation) and time_filter.op == '>' and time_filter.args[1] == Latest():
            integration_select = Select(targets=[Star()],
                                        from_table=table,
                                        where=preparation_where,
                                        order_by=order_by,
                                        limit=Constant(predictor_window),
                                        )
            integration_select.where = find_and_remove_time_filter(integration_select.where, time_filter)
            integration_selects = [integration_select]

        elif isinstance(time_filter, BinaryOperation) and time_filter.op in ('>', '>='):
            time_filter_date = time_filter.args[1]
            preparation_time_filter_op = {'>': '<=', '>=': '<'}[time_filter.op]

            preparation_time_filter = BinaryOperation(preparation_time_filter_op, args=[Identifier(predictor_time_column_name), time_filter_date])
            preparation_where2 = replace_time_filter(preparation_where2, time_filter, preparation_time_filter)
            integration_select_1 = Select(targets=[Star()],
                                          from_table=table,
                                          where=add_order_not_null(preparation_where2),
                                          order_by=order_by,
                                          limit=Constant(predictor_window))

            integration_select_2 = Select(targets=[Star()],
                                          from_table=table,
                                          where=preparation_where,
                                          order_by=order_by)

            integration_selects = [integration_select_1, integration_select_2]
        else:
            integration_select = Select(targets=[Star()],
                                        from_table=table,
                                        where=preparation_where,
                                        order_by=order_by,
                                        )
            integration_selects = [integration_select]

        if len(predictor_group_by_names) == 0:
            # ts query without grouping
            # one or multistep
            if len(integration_selects) == 1:
                select_partition_step = self.get_integration_select_step(integration_selects[0])
            else:
                select_partition_step = MultipleSteps(
                    steps=[self.get_integration_select_step(s) for s in integration_selects], reduce='union')

            # fetch data step
            data_step = self.plan.add_step(select_partition_step)
        else:
            # inject $var to queries
            for integration_select in integration_selects:
                condition = integration_select.where
                for num, column in enumerate(predictor_group_by_names):
                    cond = BinaryOperation('=', args=[Identifier(column), Constant(f'$var[{column}]')])

                    # join to main condition
                    if condition is None:
                        condition = cond
                    else:
                        condition = BinaryOperation('and', args=[condition, cond])

                integration_select.where = condition
            # one or multistep
            if len(integration_selects) == 1:
                select_partition_step = self.get_integration_select_step(integration_selects[0])
            else:
                select_partition_step = MultipleSteps(
                    steps=[self.get_integration_select_step(s) for s in integration_selects], reduce='union')

            # get groping values
            no_time_filter_query = copy.deepcopy(query)
            no_time_filter_query.where = find_and_remove_time_filter(no_time_filter_query.where, time_filter)
            select_partitions_step = self.plan_fetch_timeseries_partitions(no_time_filter_query, table, predictor_group_by_names)

            # sub-query by every grouping value
            map_reduce_step = self.plan.add_step(MapReduceStep(values=select_partitions_step.result, reduce='union', step=select_partition_step))
            data_step = map_reduce_step

        predictor_step = self.plan.add_step(
            ApplyTimeseriesPredictorStep(
                output_time_filter=time_filter,
                namespace=predictor_namespace,
                dataframe=data_step.result,
                predictor=predictor,
            )
        )

        return {
            'predictor': predictor_step,
            'data': data_step,
            'saved_limit': saved_limit,
        }


    def plan_join_two_tables(self, join):
        select_left_step = self.plan_integration_select(Select(targets=[Star()], from_table=join.left))
        select_right_step = self.plan_integration_select(Select(targets=[Star()], from_table=join.right))

        left_integration_name, left_table = self.get_integration_path_from_identifier_or_error(join.left)
        right_integration_name, right_table = self.get_integration_path_from_identifier_or_error(join.right)

        left_table_path = left_table.to_string(alias=False)
        right_table_path = right_table.to_string(alias=False)

        new_condition_args = []
        for arg in join.condition.args:
            if isinstance(arg, Identifier):
                if left_table_path in arg.parts:
                    new_condition_args.append(
                        disambiguate_integration_column_identifier(arg, left_integration_name, left_table))
                elif right_table_path in arg.parts:
                    new_condition_args.append(
                        disambiguate_integration_column_identifier(arg, right_integration_name, right_table))
                else:
                    raise PlanningException(
                        f'Wrong table or no source table in join condition for column: {str(arg)}')
            else:
                new_condition_args.append(arg)
        new_join = copy.deepcopy(join)
        new_join.condition.args = new_condition_args
        new_join.left = Identifier(left_table_path, alias=left_table.alias)
        new_join.right = Identifier(right_table_path, alias=right_table.alias)

        # FIXME: INFORMATION_SCHEMA with condition
        # clear join condition for INFORMATION_SCHEMA
        if right_integration_name == 'INFORMATION_SCHEMA':
            new_join.condition = None

        return self.plan.add_step(JoinStep(left=select_left_step.result, right=select_right_step.result, query=new_join))

    def plan_project(self, query, dataframe):
        out_identifiers = []
        for target in query.targets:
            if isinstance(target, Identifier) or isinstance(target, Star) or isinstance(target, Constant):
                out_identifiers.append(target)
            else:
                new_identifier = Identifier(str(target.to_string(alias=False)), alias=target.alias)
                out_identifiers.append(new_identifier)
        return self.plan.add_step(ProjectStep(dataframe=dataframe, columns=out_identifiers))

    def get_aliased_fields(self, targets):
        # get aliases from select target
        aliased_fields = {}
        for target in targets:
            if target.alias is not None:
                aliased_fields[target.alias.to_string()] = target
        return aliased_fields

    def plan_join(self, query, integration=None):
        join = query.from_table
        join_left = join.left
        join_right = join.right

        if isinstance(join_left, Select):
            # dbt query.
            # TODO support complex query. Only one table is supported at the moment.
            if not isinstance(join_left.from_table, Identifier):
                raise PlanningException(f'Statement not supported: {query.to_string()}')

            # move properties to upper query
            query = join_left

            if query.from_table.alias is not None:
                table_alias = query.from_table.alias.parts[0]
            else:
                table_alias = query.from_table.parts[-1]

            def add_aliases(node, is_table, **kwargs):
                if not is_table and isinstance(node, Identifier):
                    if len(node.parts) == 1:
                        # add table alias to field
                        node.parts.insert(0, table_alias)

            query_traversal(query.where, add_aliases)

            if isinstance(query.from_table, Identifier):
                if integration is not None and query.from_table.parts[0] != integration:
                    # add integration name to table
                    query.from_table.parts.insert(0, integration)

            join_left = join_left.from_table

        aliased_fields = self.get_aliased_fields(query.targets)

        recursively_check_join_identifiers_for_ambiguity(query.where)
        recursively_check_join_identifiers_for_ambiguity(query.group_by, aliased_fields=aliased_fields)
        recursively_check_join_identifiers_for_ambiguity(query.having)
        recursively_check_join_identifiers_for_ambiguity(query.order_by, aliased_fields=aliased_fields)

        if isinstance(join_left, Identifier) and isinstance(join_right, Identifier):
            if self.is_predictor(join_left) and self.is_predictor(join_right):
                raise PlanningException(f'Can\'t join two predictors {str(join_left.parts[0])} and {str(join_left.parts[1])}')

            predictor_namespace = None
            predictor = None
            table = None
            predictor_is_left = False
            if self.is_predictor(join_left):
                predictor_namespace, predictor = get_predictor_namespace_and_name_from_identifier(join_left, self.default_namespace)
                predictor_is_left = True
            else:
                table = join_left

            if self.is_predictor(join_right):
                predictor_namespace, predictor = get_predictor_namespace_and_name_from_identifier(join_right, self.default_namespace)
            else:
                table = join_right

            last_step = None
            if predictor:
                # One argument is a table, another is a predictor
                # Apply mindsdb model to result of last dataframe fetch
                # Then join results of applying mindsdb with table

                if self.predictor_metadata[predictor.to_string(alias=False)].get('timeseries'):
                    predictor_steps = self.plan_timeseries_predictor(query, table, predictor_namespace, predictor)
                else:
                    predictor_steps = self.plan_predictor(query, table, predictor_namespace, predictor)

                # add join
                # Update reference
                _, table = self.get_integration_path_from_identifier_or_error(table)
                table_alias = table.alias or Identifier(table.to_string(alias=False).replace('.', '_'))

                left = Identifier(predictor_steps['predictor'].result.ref_name,
                                   alias=predictor.alias or Identifier(predictor.to_string(alias=False)))
                right = Identifier(predictor_steps['data'].result.ref_name, alias=table_alias)

                if not predictor_is_left:
                    # swap join
                    left, right = right, left
                new_join = Join(left=left, right=right, join_type=join.join_type)

                left = predictor_steps['predictor'].result
                right = predictor_steps['data'].result
                if not predictor_is_left:
                    # swap join
                    left, right = right, left

                last_step = self.plan.add_step(JoinStep(left=left, right=right, query=new_join))

                # limit from timeseries
                if predictor_steps.get('saved_limit'):
                    last_step = self.plan.add_step(LimitOffsetStep(dataframe=last_step.result,
                                                              limit=predictor_steps['saved_limit']))

            else:
                # Both arguments are tables, join results of 2 dataframe fetches

                join_step = self.plan_join_two_tables(join)
                last_step = join_step
                if query.where:
                    # FIXME: INFORMATION_SCHEMA with Where
                    right_integration_name, _ = self.get_integration_path_from_identifier_or_error(join.right)
                    if right_integration_name == 'INFORMATION_SCHEMA':
                        ...
                    else:
                        last_step = self.plan.add_step(FilterStep(dataframe=last_step.result, query=query.where))

                if query.group_by:
                    group_by_targets = []
                    for t in query.targets:
                        target_copy = copy.deepcopy(t)
                        target_copy.alias = None
                        group_by_targets.append(target_copy)
                    last_step = self.plan.add_step(GroupByStep(dataframe=last_step.result, columns=query.group_by, targets=group_by_targets))

                if query.having:
                    last_step = self.plan.add_step(FilterStep(dataframe=last_step.result, query=query.having))

                if query.order_by:
                    last_step = self.plan.add_step(OrderByStep(dataframe=last_step.result, order_by=query.order_by))

                if query.limit is not None or query.offset is not None:
                    limit = query.limit.value if query.limit is not None else None
                    offset = query.offset.value if query.offset is not None else None
                    last_step = self.plan.add_step(LimitOffsetStep(dataframe=last_step.result, limit=limit, offset=offset))

        else:
            raise PlanningException(f'Join of unsupported objects, currently only tables and predictors can be joined.')
        return self.plan_project(query, last_step.result)

    def plan_create_table(self, query):
        if query.from_select is None:
            raise PlanningException(f'Not implemented "create table": {query.to_string()}')

        integration_name = query.name.parts[0]

        last_step = self.plan_select(query.from_select, integration=integration_name)

        # create table step
        self.plan.add_step(SaveToTable(
            table=query.name,
            dataframe=last_step,
            is_replace=query.is_replace,
        ))

    def plan_select(self, query, integration=None):
        from_table = query.from_table

        if isinstance(from_table, Identifier):
            if self.is_predictor(from_table):
                return self.plan_select_from_predictor(query)
            else:
                return self.plan_integration_select(query)
        elif isinstance(from_table, Select):
            return self.plan_integration_nested_select(query)
        elif isinstance(from_table, Join):
            return self.plan_join(query, integration=integration)
        else:
            raise PlanningException(f'Unsupported from_table {type(from_table)}')

    def plan_union(self, query):
        query1 = self.plan_select(query.left)
        query2 = self.plan_select(query.right)

        return self.plan.add_step(UnionStep(left=query1.result, right=query2.result, unique=query.unique))

    # method for compatibility
    def from_query(self, query=None):
        if query is None:
            query = self.query

        if isinstance(query, Select):
            self.plan_select(query)
        elif isinstance(query, Union):
            self.plan_union(query)
        elif isinstance(query, CreateTable):
            self.plan_create_table(query)
        else:
            raise PlanningException(f'Unsupported query type {type(query)}')

        return self.plan

    def prepare_steps(self, query):
        statement_planner = PreparedStatementPlanner(self)

        # return generator
        return statement_planner.prepare_steps(query)

    def execute_steps(self, params=None):
        statement_planner = PreparedStatementPlanner(self)

        # return generator
        return statement_planner.execute_steps(params)

    # def fetch(self, row_count):
    #     statement_planner = PreparedStatementPlanner(self)
    #     return statement_planner.fetch(row_count)
    #
    # def close(self):
    #     statement_planner = PreparedStatementPlanner(self)
    #     return statement_planner.close()

    def get_statement_info(self):
        statement_planner = PreparedStatementPlanner(self)

        return statement_planner.get_statement_info()




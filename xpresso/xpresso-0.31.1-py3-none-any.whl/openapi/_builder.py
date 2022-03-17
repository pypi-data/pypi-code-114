import inspect
from http import HTTPStatus
from typing import Any, Dict, Iterable, List, Mapping, Optional, Set, Tuple, Union

from di.container import Container
from pydantic import BaseConfig
from pydantic.fields import ModelField
from pydantic.schema import field_schema, get_flat_models_from_fields
from pydantic.schema import get_model_name_map as get_model_name_map_pydantic
from starlette.responses import Response

from xpresso._utils.compat import get_args, get_origin, get_type_hints
from xpresso._utils.routing import VisitedRoute
from xpresso.binders import dependants as binder_dependants
from xpresso.openapi import models
from xpresso.openapi._constants import REF_PREFIX
from xpresso.openapi._utils import merge_response_specs, parse_examples
from xpresso.responses import ResponseModel, ResponseSpec, TypeUnset
from xpresso.routing.operation import Operation
from xpresso.routing.pathitem import Path
from xpresso.routing.router import Router

ModelNameMap = Dict[type, str]

Routes = Mapping[str, Tuple[Path, Mapping[str, Operation]]]


validation_error_definition = {
    "title": "ValidationError",
    "type": "object",
    "properties": {
        "loc": {
            "title": "Location",
            "type": "array",
            "items": {"oneOf": [{"type": "string"}, {"type": "integer"}]},
        },
        "msg": {"title": "Message", "type": "string"},
        "type": {"title": "Error Type", "type": "string"},
    },
    "required": ["loc", "msg", "type"],
}

validation_error_response_definition = {
    "title": "HTTPValidationError",
    "type": "object",
    "properties": {
        "detail": {
            "title": "Detail",
            "type": "array",
            "items": {"$ref": f"{REF_PREFIX}ValidationError"},
        }
    },
}

validation_error_response = models.Response(
    description="Validation Error",
    content={
        "application/json": models.MediaType(
            schema=models.Schema.parse_obj({"$ref": f"{REF_PREFIX}HTTPValidationError"})  # type: ignore
        )
    },
)

status_code_range_descriptions = {
    "1XX": "Information",
    "2XX": "Success",
    "3XX": "Redirection",
    "4XX": "Client Error",
    "5XX": "Server Error",
    "DEFAULT": "Default Response",
}

status_code_descriptions = {
    str(v.value): v.phrase for v in HTTPStatus.__members__.values()
}


def get_model_name_map(unique_models: Set[type]) -> Dict[type, str]:
    # this works with any class, but Pydantic types it as if it only works with Pydantic models
    # if this at some point breaks, we'll just implement it in this function
    return get_model_name_map_pydantic({model for model in unique_models if hasattr(model, "__name__")})  # type: ignore[arg-type]


def get_parameters(
    deps: List[binder_dependants.ParameterBinder],
    model_name_map: ModelNameMap,
    schemas: Dict[str, Any],
) -> Optional[List[models.ConcreteParameter]]:
    parameters: List[models.ConcreteParameter] = [
        dependant.openapi.get_openapi_parameter(
            model_name_map=model_name_map, schemas=schemas
        )
        for dependant in deps
        if dependant.openapi and dependant.openapi.include_in_schema
    ]

    if parameters:
        return list(sorted(parameters, key=lambda param: param.name))
    return None


def get_request_body(
    dependant: binder_dependants.BodyBinder,
    model_name_map: ModelNameMap,
    schemas: Dict[str, Any],
) -> models.RequestBody:
    if dependant.openapi and dependant.openapi.include_in_schema:
        return dependant.openapi.get_openapi_body(
            model_name_map=model_name_map, schemas=schemas
        )
    return models.RequestBody(content={})


def get_schema(
    type_: type, model_name_map: ModelNameMap, schemas: Dict[str, Any]
) -> models.Schema:
    field = ModelField.infer(
        name="Response",
        value=...,
        annotation=type_,
        class_validators=None,
        config=BaseConfig,
    )
    flat_models = get_flat_models_from_fields([field], known_models=set())
    model_name_map = get_model_name_map(flat_models)
    schema, new_schemas, _ = field_schema(field, model_name_map=model_name_map, ref_prefix=REF_PREFIX)  # type: ignore[arg-type]
    schemas.update(new_schemas)
    return models.Schema(**schema)


def description_from_user_input_or_status_code(
    description: Optional[str], status_code: str
) -> str:
    if description:
        return description
    if status_code in status_code_descriptions:
        return status_code_descriptions[status_code]
    if status_code in status_code_range_descriptions:
        return status_code_range_descriptions[status_code]
    raise ValueError(f'Unknown status code "{status_code}"')


def get_response_model(
    spec: ResponseSpec,
    status_code: str,
    model_name_map: ModelNameMap,
    schemas: Dict[str, Any],
) -> models.Response:
    headers = {
        header: models.ResponseHeader(description=header_or_description)
        if isinstance(header_or_description, str)
        else header_or_description
        for header, header_or_description in (spec.headers or {}).items()
    } or None
    content = {
        k: v if isinstance(v, ResponseModel) else ResponseModel(v)
        for k, v in (spec.content or {}).items()
    }
    examples = {
        k: parse_examples(v.examples) if v.examples is not None else None
        for k, v in content.items()
    }
    schemas = {
        k: get_schema(v.model, model_name_map, schemas)
        if v.model is not TypeUnset
        else None
        for k, v in content.items()
    }
    return models.Response(
        description=description_from_user_input_or_status_code(
            spec.description, status_code
        ),
        headers=headers,  # type: ignore[arg-type]
        content={
            k: models.MediaType(
                schema=schemas[k],  # type: ignore
                examples=examples[k],
            )
            for k in content
        }
        or None,
    )


def get_responses(
    response_specs: Mapping[str, ResponseSpec],
    model_name_map: ModelNameMap,
    schemas: Dict[str, Any],
) -> Dict[str, models.Response]:
    responses: Dict[str, models.Response] = {}
    for status, response_spec in response_specs.items():
        if (
            status in responses
            or f"{status[0]}XX" in responses
            or (
                status.endswith("XX")
                and any(str(s).startswith(status[0]) for s in responses)
            )
        ):
            raise ValueError("Duplicate response status codes are not allowed")
        responses[status] = get_response_model(
            response_spec, status, model_name_map, schemas
        )
    return responses


def is_response(tp: type) -> bool:
    return inspect.isclass(tp) and issubclass(tp, Response)


def get_operation(
    route: Operation,
    model_name_map: ModelNameMap,
    components: Dict[str, Any],
    tags: List[str],
    response_specs: Dict[str, ResponseSpec],
) -> models.Operation:
    data: Dict[str, Any] = {
        "tags": tags or None,
        "summary": route.summary,
        "description": route.description,
        "deprecated": route.deprecated,
        "servers": route.servers or None,
        "external_docs": route.external_docs,
    }
    docstring = getattr(route.endpoint, "__doc__", None)
    if docstring and not data["description"]:
        data["description"] = docstring
    schemas: Dict[str, Any] = {}
    route_dependant = route.dependant
    assert route_dependant is not None
    parameters = get_parameters(
        [
            dep
            for dep in route_dependant.get_flat_subdependants()
            if isinstance(dep, binder_dependants.ParameterBinder)
        ],
        model_name_map,
        schemas,
    )
    if parameters:
        data["parameters"] = parameters
    body_dependants = [
        dep
        for dep in route_dependant.get_flat_subdependants()
        if isinstance(dep, binder_dependants.BodyBinder)
    ]
    if len(body_dependants) > 1:
        raise ValueError("Only 1 top level body is allowed in OpenAPI specs")
    body_dependant = next(iter(body_dependants), None)
    if body_dependant is not None:
        data["requestBody"] = get_request_body(body_dependant, model_name_map, schemas)
    # merge in the default response spec
    response_model = route.response_model
    if response_model is TypeUnset:
        sig_return = inspect.signature(route.endpoint).return_annotation
        if sig_return is not inspect.Parameter.empty:
            response_annotation = get_type_hints(route.endpoint)["return"]
            if (
                # get_type_hints returns type(None)
                # if the func is () -> None we don't add a response model
                # it is rare to want to _document_ "null" as the response model
                sig_return
                is None
            ) or (
                # this is a special case for () -> FileResponse and the like
                is_response(response_annotation)
                or get_origin(response_annotation) is Union
                and any(is_response(tp) for tp in get_args(response_annotation))
            ):
                response_annotation = TypeUnset
            if response_annotation is not TypeUnset:
                response_model = response_annotation
    default_content = {
        route.response_media_type: ResponseModel(
            model=response_model,
            examples=route.response_examples,
        )
    }
    route_response_status_code = str(route.response_status_code)
    route_response_description = description_from_user_input_or_status_code(
        route.response_description, route_response_status_code
    )
    if route_response_status_code in response_specs:
        if response_specs[route_response_status_code].content:
            content = response_specs[route_response_status_code].content
        else:
            content = default_content
        response_specs[route_response_status_code] = merge_response_specs(
            ResponseSpec(
                description=route_response_description,
                content=content,
                headers=route.response_headers,
            ),
            response_specs[route_response_status_code],
        )
    else:
        response_specs[route_response_status_code] = ResponseSpec(
            description=route_response_description,
            content=default_content,
            headers=route.response_headers,
        )
    data["responses"] = get_responses(
        response_specs=response_specs,
        model_name_map=model_name_map,
        schemas=schemas,
    )
    if schemas:
        components["schemas"] = {**components.get("schemas", {}), **schemas}
    if ((data.get("parameters", None) or data.get("requestBody", None))) and all(
        status not in data["responses"] for status in ("422", "4XX", "default")
    ):
        data["responses"]["422"] = validation_error_response

        if "ValidationError" not in schemas:
            components["schemas"] = components.get("schemas", None) or {}
            components["schemas"].update(
                {
                    "ValidationError": validation_error_definition,
                    "HTTPValidationError": validation_error_response_definition,
                }
            )
    return models.Operation(**data)


def merge_node_openapi_metadata(
    node: Union[Router, Path, Operation],
    tags: List[str],
    responses: Dict[str, ResponseSpec],
) -> Tuple[List[str], Dict[str, ResponseSpec]]:
    new_responses: Dict[str, ResponseSpec] = responses.copy()
    for status_code, response in node.responses.items():
        status_code_str = str(status_code)
        if status_code not in responses:
            new_responses[status_code_str] = response
        else:
            new_responses[status_code_str] = merge_response_specs(
                responses[status_code_str], response
            )
    return [*tags, *node.tags], new_responses


def get_paths_items(
    visitor: Iterable[VisitedRoute[Any]],
    model_name_map: ModelNameMap,
    components: Dict[str, Any],
) -> Dict[str, models.PathItem]:
    paths: "Dict[str, models.PathItem]" = {}
    for visited_route in visitor:
        if isinstance(visited_route.route, Path):
            path_item = visited_route.route
            if not path_item.include_in_schema:
                continue
            tags: "List[str]" = []
            include_in_schema = True
            responses: "Dict[str, ResponseSpec]" = {}
            for node in visited_route.nodes:
                if isinstance(node, Router):
                    if not node.include_in_schema:
                        include_in_schema = False
                        break
                    tags, responses = merge_node_openapi_metadata(node, tags, responses)
            if not include_in_schema:
                continue
            tags, responses = merge_node_openapi_metadata(path_item, tags, responses)
            operations: "Dict[str, models.Operation]" = {}
            for method, operation in path_item.operations.items():
                if not operation.include_in_schema:
                    continue
                operation_tags, operation_responses = merge_node_openapi_metadata(
                    operation, tags, responses
                )
                operations[method.lower()] = get_operation(
                    operation,
                    model_name_map=model_name_map,
                    components=components,
                    tags=operation_tags,
                    response_specs=operation_responses,
                )
            paths[visited_route.path] = models.PathItem(
                description=visited_route.route.description,
                summary=visited_route.route.summary,
                servers=list(visited_route.route.servers) or None,
                **operations,  # type: ignore[arg-type]
            )  # type: ignore  # for Pylance
    return {k: paths[k] for k in sorted(paths.keys())}


def filter_routes(visitor: Iterable[VisitedRoute[Any]]) -> Routes:
    res: Dict[str, Tuple[Path, Dict[str, Operation]]] = {}
    for visited_route in visitor:
        if isinstance(visited_route.route, Path):
            path_item = visited_route.route
            if not path_item.include_in_schema:
                continue
            operations: Dict[str, Operation] = {
                method.lower(): operation
                for method, operation in path_item.operations.items()
                if operation.include_in_schema
            }

            res[visited_route.path] = (path_item, operations)
    return res


def get_flat_models(routes: Routes) -> Set[type]:
    res: Set[type] = set()
    for _, operations in routes.values():
        for operation in operations.values():
            dependant = operation.dependant
            flat_dependencies = dependant.get_flat_subdependants()
            for dep in flat_dependencies:
                if isinstance(
                    dep,
                    (binder_dependants.ParameterBinder, binder_dependants.BodyBinder),
                ):
                    if dep.openapi is not None:
                        res.update(dep.openapi.get_models())
            for response in operation.responses.values():
                for response_model in (response.content or {}).values():
                    if (
                        isinstance(response_model, ResponseModel)
                        and response_model.model is not TypeUnset
                    ):
                        res.add(response_model.model)
    return res


def generate_openapi(
    visitor: Iterable[VisitedRoute[Any]],
    container: Container,
    version: str,
    info: models.Info,
    servers: Optional[Iterable[models.Server]],
) -> models.OpenAPI:
    visitor = list(visitor)
    routes = filter_routes(visitor)
    flat_models = get_flat_models(routes)
    model_name_map = get_model_name_map(flat_models)
    components: Dict[str, Any] = {}
    paths = get_paths_items(visitor, model_name_map, components)
    return models.OpenAPI(
        openapi=version,
        info=info,
        paths=paths,  # type: ignore[arg-type]
        components=models.Components(**components) if components else None,
        servers=list(servers) if servers else None,
    )

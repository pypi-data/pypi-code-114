# -*- coding: utf-8 -*-
import datetime
from typing import Optional, List

from pip_services3_commons.commands import CommandSet, Command
from pip_services3_commons.convert import TypeCode
from pip_services3_commons.run import Parameters
from pip_services3_commons.validate import ObjectSchema, ArraySchema

from .IFireMapController import IFireMapController
from ..data.version1 import LocationV1, FireMapUpdateV1, FireMapUpdateV1Schema


class FireMapCommandSet(CommandSet):

    def __init__(self, controller: IFireMapController):
        super().__init__()

        self.__controller = controller

        self.add_command(self.__make_get_tiles_command())
        self.add_command(self.__make_update_tiles_command())

    def __make_get_tiles_command(self):
        def handler(correlation_id: Optional[str], args: Parameters):
            of = LocationV1(args.get_as_nullable_float('flat'), args.get_as_nullable_float('flng'))
            to = LocationV1(args.get_as_nullable_float('tlat'), args.get_as_nullable_float('tlng'))
            zoom = args.get_as_nullable_integer('zoom')
            return self.__controller.get_tiles(correlation_id, of, to, zoom)

        return Command('get_tiles',
                       ObjectSchema()
                       .with_optional_property('flat', TypeCode.Float)
                       .with_optional_property('flng', TypeCode.Float)
                       .with_optional_property('tlat', TypeCode.Float)
                       .with_optional_property('tlng', TypeCode.Float)
                       .with_optional_property('zoom', TypeCode.Integer),
                       handler
                       )

    def __make_update_tiles_command(self):
        def handler(correlation_id: Optional[str], args: Parameters):
            updates = args.get('updates')
            updates_list: List[FireMapUpdateV1] = []

            if isinstance(updates[0], dict):
                for update in updates:
                    if update['time'][-1] in ['Z', 'z']:
                        update['time'] = datetime.datetime.fromisoformat(update['time'][:-1])
                    else:
                        update['time'] = datetime.datetime.fromisoformat(update['time'])
                    updates_list.append(FireMapUpdateV1(**update))
                updates = updates_list

            return self.__controller.update_tiles(correlation_id, updates)

        return Command('update_tiles',
                       ObjectSchema(True)
                       .with_required_property('updates', ArraySchema(FireMapUpdateV1Schema())),
                       handler
                       )

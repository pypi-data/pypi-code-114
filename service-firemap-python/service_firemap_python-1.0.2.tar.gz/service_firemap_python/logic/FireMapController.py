# -*- coding: utf-8 -*-

import datetime

from typing import Optional, List

from pip_services3_commons.commands import ICommandable, CommandSet
from pip_services3_commons.config import IConfigurable, ConfigParams
from pip_services3_commons.convert import JsonConverter
from pip_services3_commons.data import FilterParams, PagingParams
from pip_services3_commons.refer import IReferenceable, IReferences, Descriptor
from pip_services3_messaging.queues import IMessageQueue, MessageEnvelope

from .FireMapCommandSet import FireMapCommandSet
from .IFireMapController import IFireMapController
from ..data.version1 import LocationV1, FireMapTileV1, FireMapUpdateV1, FireMapZoomV1, FireMapUpdateTypeV1
from ..data.version1.FireMapTileBlockV1 import FireMapTileBlockV1
from ..map_utils import FireMapUtil
from ..persistence.IFireMapPersistence import IFireMapPersistence


class FireMapController(IFireMapController, IConfigurable, IReferenceable, ICommandable):

    def __init__(self):
        self.__persistence: IFireMapPersistence = None
        self.__command_set: FireMapCommandSet = None
        self.__message_queue: IMessageQueue = None

    def configure(self, config: ConfigParams):
        pass

    def set_references(self, references: IReferences):
        self.__persistence = references.get_one_required(Descriptor(
            'eic-stopfires-services-firemap', 'persistence', '*', '*', '1.0'))

        self.__message_queue = references.get_one_optional(
            Descriptor('pip-services', 'message-queue', '*', '*', '1.0')
        )

    def get_command_set(self) -> CommandSet:
        self.__command_set = self.__command_set or FireMapCommandSet(self)
        return self.__command_set

    def get_tiles(self, correlation_id: Optional[str], of: Optional[LocationV1], to: Optional[LocationV1],
                  zoom: Optional[int]) -> List[FireMapTileV1]:
        filter_params = FilterParams.from_tuples(
            'flng', None if not of else of.long,
            'flat', None if not of else of.lat,
            'tlng', None if not to else to.long,
            'tlat', None if not to else to.lat,
            'zoom', zoom
        )

        page = self.__persistence.get_tile_blocks_by_filter(correlation_id, filter_params, PagingParams())

        tiles: List[FireMapTileV1] = []

        for block in page.data:
            tiles.extend(block.tiles.values())

        return tiles

    def update_tiles(self, correlation_id: Optional[str], updates: List[FireMapUpdateV1]):
        coordinates = []

        for update in updates:
            coordinates.append(f'{update.lat};{update.long}')

        # get tile blocks for update
        update_blocks = self.__persistence.get_tile_blocks_by_filter(correlation_id,
                                                                     FilterParams.from_tuples('coordinates',
                                                                                              coordinates),
                                                                     PagingParams()).data

        absent_zooms: List[int] = [e.value for e in FireMapZoomV1]

        for update in updates:
            current_update_blocks: List[FireMapTileBlockV1] = []

            index = 0
            for block in update_blocks:
                # check if update coordinates in block coordinates
                if block.flng <= update.long <= block.tlng and block.tlat <= update.lat <= block.flat:
                    # find absent zooms
                    current_update_blocks.append(block)
                    absent_zooms = list(filter(lambda z: z != block.zoom, absent_zooms))
                    update_blocks[index] = None
                index += 1

            update_blocks = list(filter(lambda e: e is not None, update_blocks))

            # if block is not created, or some absent
            if len(absent_zooms) > 0:
                new_blocks = self.__create_blocks(update.lat, update.long, absent_zooms)
                current_update_blocks.extend(new_blocks)

            # sort by zoom for updating from small to big
            current_update_blocks.sort(key=lambda b: b.zoom)

            # update blocks for all zooms
            for block in current_update_blocks:

                # compose id by zoom
                loc = FireMapUtil.get_locator(LocationV1(update.lat, update.long))
                id = FireMapUtil.compose_tile_loc_by_zoom(loc, block.zoom)

                # update current based on states of the children
                if update.type is None or self.__can_update_block(block, current_update_blocks, update.type):
                    if update.type == FireMapUpdateTypeV1.CLEAR:
                        block.tiles[id].clear = update.time
                        block.tiles[id].cdrone = update.drone_id
                    elif update.type == FireMapUpdateTypeV1.SMOKE:
                        block.tiles[id].smoke = update.time
                        block.tiles[id].sdrone = update.drone_id
                    elif update.type == FireMapUpdateTypeV1.FIRE:
                        block.tiles[id].fire = update.time
                        block.tiles[id].fdrone = update.drone_id

                    block.tiles[id].pdrone = update.drone_id

                # calc peoples on child blocks
                people_count: int = update.people

                if block.zoom != FireMapZoomV1.Zoom50m:
                    people_count = 0
                    filtered = list(filter(lambda b: b.zoom + 1 == block.zoom, current_update_blocks))
                    child_block: FireMapTileBlockV1 = None if len(filtered) < 1 else filtered[0]

                    if child_block is not None:
                        for tile in child_block.tiles.values():
                            people_count += 0 if not tile.people_count else tile.people_count

                # update peoples count for all statuses
                block.tiles[id].people = update.time
                block.tiles[id].people_count = people_count

                if self.__message_queue is not None:
                    message = MessageEnvelope(correlation_id, 'FireMapTileV1', JsonConverter.to_json(block.tiles[id]))
                    self.__message_queue.send(correlation_id, message)

            update_blocks.extend(current_update_blocks)

        self.__persistence.update_tile_blocks(correlation_id, update_blocks)

    def __create_blocks(self, lat: float, long: float, zooms: List[int]) -> List[FireMapTileBlockV1]:
        blocks: List[FireMapTileBlockV1] = []
        zooms = zooms or [e.value for e in FireMapZoomV1]

        locator = FireMapUtil.get_locator(LocationV1(lat, long))

        for tile_zoom in zooms:
            block_zoom = tile_zoom + 1
            block_coord = FireMapUtil.get_locator_coordinates(locator, block_zoom)
            # calc id as block locator
            center = FireMapUtil.calc_center_coordinates(LocationV1(block_coord[0].lat, block_coord[0].long),
                                                         LocationV1(block_coord[1].lat, block_coord[1].long))

            loc_of_center = FireMapUtil.get_locator(LocationV1(center.lat, center.long))
            loc_of_block = (FireMapUtil.compose_tile_loc_by_zoom(loc_of_center, block_zoom) + '_' + str(
                block_zoom - 1)).upper()

            block = FireMapTileBlockV1(
                id=loc_of_block,
                zoom=tile_zoom,
                flat=block_coord[0].lat,
                flng=block_coord[0].long,
                tlat=block_coord[1].lat,
                tlng=block_coord[1].long,
                tiles={},
            )

            # if it biggest block
            iterations = 0

            if tile_zoom == FireMapZoomV1.Zoom50m:
                iterations = 24  # 576 tiles for 'AA-XX'
            elif tile_zoom == FireMapZoomV1.Zoom1km:
                iterations = 10  # 100 tiles for '00-99'
            elif tile_zoom == FireMapZoomV1.Zoom20km:
                iterations = 24  # 576 tiles for 'AA-XX'
            elif tile_zoom == FireMapZoomV1.Zoom50km:
                iterations = 10  # 100 tiles for '00-99'
            elif tile_zoom == FireMapZoomV1.Zoom100km:
                iterations = 18  # 324 tiles for 'AA-XX'

            # fill all current block tiles
            for i in range(iterations):
                for j in range(iterations):
                    tile_locator = FireMapUtil.get_loc_by_zoom(locator, block_zoom)

                    if len(tile_locator) in [2, 6]:
                        tile_locator += str(i) + str(j)
                    elif len(tile_locator) in [0, 4, 8]:
                        tile_locator += chr(i + 65) + chr(j + 65)

                    tile_coord = FireMapUtil.get_locator_coordinates(tile_locator, tile_zoom)

                    # calc tile id as locator
                    id = FireMapUtil.compose_tile_loc_by_zoom(tile_locator, tile_zoom)

                    tile = FireMapTileV1(
                        id=id,
                        flat=tile_coord[0].lat,
                        flng=tile_coord[0].long,
                        tlat=tile_coord[1].lat,
                        tlng=tile_coord[1].long,
                        zoom=block.zoom
                    )

                    block.tiles[id] = tile

            blocks.append(block)

        return blocks

    def __can_update_block(self, curr_block: FireMapTileBlockV1, blocks: List[FireMapTileBlockV1], type: str) -> bool:
        child_blocks = filter(lambda b: b.zoom < curr_block.zoom, blocks)
        checked = 0
        count_of_tiles = 0

        for child_block in child_blocks:
            count_of_tiles += len(child_block.tiles)

            for id in child_block.tiles:
                # if settled values updated
                child_block.tiles[id] = self.__default_datetime(child_block.tiles[id])

                if type == FireMapUpdateTypeV1.CLEAR:
                    if (child_block.tiles[id].clear >= child_block.tiles[id].smoke and
                            child_block.tiles[id].clear >= child_block.tiles[id].fire):
                        checked += 1
                elif type == FireMapUpdateTypeV1.SMOKE:
                    if child_block.tiles[id].smoke >= child_block.tiles[id].fire:
                        checked += 1
                elif type == FireMapUpdateTypeV1.FIRE:
                    child_block.tiles[id] = self.__default_datetime(child_block.tiles[id], True)
                    return True

                child_block.tiles[id] = self.__default_datetime(child_block.tiles[id], True)

        # if checked all blocks
        return count_of_tiles == checked

    def __default_datetime(self, tile: FireMapTileV1, set_none=False):
        default = datetime.datetime(1, 1, 1)

        if set_none:
            if tile.clear == default:
                tile.clear = None
            if tile.smoke == default:
                tile.smoke = None
            if tile.fire == default:
                tile.fire = None
        else:
            if not tile.clear:
                tile.clear = default
            if not tile.smoke:
                tile.smoke = default
            if not tile.fire:
                tile.fire = default
        return tile

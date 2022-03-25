# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from ..base import Base


class Assets(Base):

    """Used to sync assets from a source instance to a destination instance of Swimlane
    """

    def __get_asset_parameters(self, source: dict, destination: dict):
        self.__logger.info(f"Getting asset parameters from source.")
        if source.get('parameters') and destination.get('parameters'):
            if source['parameters'].get('$type'):
                source['parameters'].pop('$type')
            if destination['parameters'].get('$type'):
                destination['parameters'].pop('$type')
            for key,val in source['parameters'].items():
                if not destination['parameters'].get(key):
                    destination['parameters'].update({
                        key: None
                    })
            return destination['parameters']

    def __update_asset(self, asset):
        for dest_asset in self.destination_instance.get_assets():
            if asset.get('uid') and dest_asset.get('uid') and asset['uid'] == dest_asset['uid']:
                if asset.get('version') and dest_asset.get('version') and asset['version'] == dest_asset['version']:
                    self.__logger.info(f"Asset '{asset['name']}' already exists on destination. Skipping...")
                    return 
                else:
                    self.__logger.info(f"Asset '{asset['name']}' is different. Updating...")
                    dest_asset['parameters'] = self.__get_asset_parameters(asset, dest_asset)
                    self.destination_instance.update_asset(dest_asset['id'], dest_asset)
                    self.__logger.info(f"Successfully updated asset '{asset['name']}' on destination.")

    def sync_asset(self, asset: dict):
        """This method will create (add) a single asset from a source instance to a destination instance.

        Currently we are only adding assets and NOT updating them but this functionality may expand in the future.

        Args:
            asset (dict): A single Swimlane asset dictionary from the Swimlane API
        """
        if not self._is_in_include_exclude_lists(asset['name'], 'assets'):
            self.__logger.info(f"Processing asset '{asset['name']}'.")
            if not hasattr(self, 'dest_assets'):
                self.dest_assets = [x['name'] for x in self.destination_instance.get_assets()]
            if asset['name'] not in self.dest_assets:
                self.__logger.info(f"Asset '{asset['name']}' was not found on destination.")
                resp = self.destination_instance.add_asset(asset)
                self.__logger.info(f"Asset '{asset['name']}' was successfully added to destination.")
            else:
                self.__logger.info(f"Asset '{asset['name']}' already exists on destination. Skipping")

    def sync(self):
        """This method is used to sync (create) all assets from a source instance to a destination instance
        """
        self.__logger.info(f"Attempting to sync assets from '{self.source_host}' to '{self.dest_host}'")
        self.dest_assets = [x['name'] for x in self.destination_instance.get_assets()]
        for asset in self.source_instance.get_assets():
            self.sync_asset(asset=asset)

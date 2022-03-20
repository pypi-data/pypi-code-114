import json
import mimetypes
import os
import uuid
from glob import glob
from pathlib import Path

import boto3
from loguru import logger
from tqdm import tqdm

from .callbacks import ProgressPercentage


class SpacesClient:

    def __init__(self, region, space_name):
        self.region = region
        self.space_name = space_name

    def connect(self):
        session = boto3.session.Session()
        client = session.client(
            's3',
            endpoint_url=f'https://{self.region}.digitaloceanspaces.com',
            region_name=self.region,
            aws_access_key_id=os.environ['SPACES_KEY_ID'],
            aws_secret_access_key=os.environ['SPACES_SECRET'])

        origin_domain = f'https://{self.space_name}.{self.region}.digitaloceanspaces.com'
        subdomain = os.getenv('SUBDOMAIN')
        return client, (origin_domain, subdomain)


class Spaces(SpacesClient):

    def __init__(self, region, space_name):
        self.region = region
        self.space_name = space_name
        self.client, self.domain = super().connect()
        self.verbose = 0

    def list_objects(self, pprint=False, simple=False, force_return=False):
        objects = self.client.list_objects(Bucket=self.space_name)
        if simple:
            objects = [{
                'name': obj['Key'],
                'last_modified': obj['LastModified'],
                'size': obj['Size']
            } for obj in objects['Contents']]
        if pprint or self.verbose == 1:
            print(json.dumps(objects, indent=4, default=str))
            if force_return:
                return objects
        else:
            return objects

    def download_file(self, file_name, output_path=None):
        if not output_path:
            output_path = f'{Path.cwd()}/{Path(file_name).name}'

        if file_name.startswith('http'):
            file_name = Path(file_name).name
        res = self.client.download_file(self.space_name, file_name,
                                        output_path)
        if self.verbose == 1:
            logger.info(output_path)
        return output_path

    def _upload(self,
                file_path,
                public=True,
                dest_name=None,
                subdomain_url=False,
                duplicates_policy='rename'):
        content_type = mimetypes.guess_type(file_path, strict=False)[0]
        if not content_type:
            content_type = ''
        ExtraArgs = {'ContentType': content_type}
        if public:
            ExtraArgs = {'ACL': 'public-read', 'ContentType': content_type}

        if not dest_name:
            dest_name = Path(file_path).name

        try:
            self.client.get_object(Bucket=self.space_name,
                                   Key=Path(file_path).name)
            _dest_name = dest_name
            if duplicates_policy == 'rename':
                dest_name = f'{Path(dest_name).stem}-{uuid.uuid4().hex[:8]}{Path(dest_name).suffix}'
                if self.verbose == 1:
                    logger.debug(f'Renamed {_dest_name} ==> {dest_name}')
            if duplicates_policy == 'reject':
                logger.warning('Duplicate file name. Skipped.')
                return
            if duplicates_policy == 'error':
                raise FileExistsError(
                    'Filename already exists in the remote bucket!')
        except self.client.exceptions.NoSuchKey:
            pass

        self.client.upload_file(file_path,
                                self.space_name,
                                dest_name,
                                ExtraArgs=ExtraArgs,
                                Callback=ProgressPercentage(file_path))
        print()
        if subdomain_url and self.domain[1]:
            if self.verbose == 1:
                logger.info(f'{self.domain[1]}/{dest_name}')
            return f'{self.domain[1]}/{dest_name}'
        if self.verbose == 1:
            logger.info(f'{self.domain[0]}/{dest_name}')
        return f'{self.domain[0]}/{dest_name}'

    def upload_file(self, file_path, **kwargs):
        return self._upload(file_path, **kwargs)

    def upload_many(self, _input, **kwargs):
        if isinstance(_input, list):
            assert all([Path(x).exists() for x in _input
                        ]), 'Some files in the list do not exist!'
        elif isinstance(_input, str):
            assert Path(_input).is_dir(
            ), 'Pass either a list of files or a directory path!'
            _input = glob(f'{_input}/*')

        result = []
        for item in tqdm(_input, desc='Total uploaded files'):
            result.append(self._upload(item, **kwargs))
        return result

    def delete_object(self, object_key):
        if object_key.startswith('http'):
            object_key = Path(object_key).name
        res = self.client.delete_object(Bucket=self.space_name, Key=object_key)
        if self.verbose == 1:
            logger.info(res)
        return res

    # Aliases
    list_files = list_objects
    download = download_file
    upload = upload_file
    upload_files = upload_many
    delete = delete_object

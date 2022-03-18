from __future__ import unicode_literals
from datetime import datetime
import yt_dlp
import requests
import re
import tempfile
from PIL import Image
from io import BytesIO
from pathlib import Path
import json
import time
import getpass

class BasketCase:
    def __init__(self):
        self._session = requests.Session()

        self._output_base = f'{Path.cwd()!s}/basketcase_{datetime.now()!s}'
        self._output_images = self._output_base + '/images'
        self._output_videos = self._output_base + '/videos'

    def fetch(self, target_urls):
        resources = self._scan(target_urls)

        if resources['images'] or resources['videos']:
            self._prepare_output()

            for index, resource in resources['images'].items():
                self._get_image(resource)
            
            self._get_videos(resources['videos'])
        else:
            print('Nothing to download.')

    def login(self, username=None, password=None, two_factor_code=None):
        login_data = None

        with self._session.get('https://www.instagram.com/accounts/login/') as response:
            login_data = re.search(r'window\._sharedData\s*=\s*({.+?});', response.text)

        if not login_data:
            raise RuntimeError('Failed to obtain JSON data from login page')
        
        login_data = json.loads(login_data.group(1))

        custom_headers = {
            'X-ASBD-ID': '198387',
            'X-CSRFToken': login_data['config']['csrf_token'],
            'X-IG-App-ID': '936619743392459',
            'X-IG-WWW-Claim': '0',
            'X-Instagram-AJAX': login_data['rollout_hash'],
            'X-Requested-With': 'XMLHttpRequest'
        }

        if not username:
            username = input('Username: ')
        
        if not password:
            password = getpass.getpass()

        with self._session.post('https://www.instagram.com/accounts/login/ajax/', data={
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}',
            'username': username,
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'stopDeletionNonce': '',
            'trustedDeviceRecords': '{}'
        }, headers=custom_headers) as response:
            json_response = response.json()

            if 'authenticated' in json_response and json_response['authenticated']:
                print('Authentication successful')
            elif 'two_factor_required' in json_response:
                if not two_factor_code:
                    two_factor_code = input('Two factor authentication code: ')

                with self._session.post('https://www.instagram.com/accounts/login/ajax/two_factor/', data={
                    'identifier': json_response['two_factor_info']['two_factor_identifier'],
                    'trust_signal': 'true',
                    'username': username,
                    'verificationCode': two_factor_code,
                    'verification_method': '3', # is 3 == totp?
                    'queryParams': '{"next":"/"}'
                }, headers=custom_headers) as response:
                    json_response = response.json()

                    if 'authenticated' in json_response and json_response['authenticated']:
                        print('Authentication successful')
                    else:
                        raise RuntimeError('Authentication failed')
            else:
                raise RuntimeError('Authentication failed')

    def _prepare_output(self):
        Path(self._output_images).mkdir(parents=True, exist_ok=True)
        Path(self._output_videos).mkdir(parents=True, exist_ok=True)

    def _scan(self, target_urls):
        """
        Scrape the HTML page to find direct links to resources
        """
        resources = {
            'images': dict(),
            'videos': set()
        }

        print('Scanning the targets. This can take a while.')

        for target_url in target_urls:
            json_string = None

            with self._session.get(target_url, timeout=10) as request:
                json_string = re.search(r'window\.__additionalDataLoaded\s*\(\s*[^,]+,\s*({.+?})\s*\);', request.text)

                if not json_string:
                    raise RuntimeError(f'JSON string not found at {target_url}')

            json_data = json.loads(json_string.group(1))

            page = json_data['items'][0]

            if 'carousel_media' in page:
                carousel_items = page['carousel_media']

                for carousel_item in carousel_items:
                    image_url = carousel_item['image_versions2']['candidates'][0]['url']
                    image_id = carousel_item['id']

                    resources['images'][image_url] = {
                        'url': image_url,
                        'id': image_id
                    }

                    if 'video_versions' in carousel_item:
                        video_url = carousel_item['video_versions'][0]['url']

                        resources['videos'].add(video_url)
            else:
                if 'image_versions2' not in page:
                    raise RuntimeError(f'Unrecognized JSON structure at {target_url}')
                
                image_url = page['image_versions2']['candidates'][0]['url']
                image_id = page['id']

                resources['images'][image_url] = {
                    'url': image_url,
                    'id': image_id
                }

                if 'video_versions' in page:
                    video_url = page['video_versions'][0]['url']

                    resources['videos'].add(video_url)

        return resources

    def _get_image(self, resource):
        print(f'Downloading image: {resource["url"]}')

        image = None

        with self._session.get(resource['url'], timeout=10) as request:
            # Build image from binary response data
            image = Image.open(BytesIO(request.content))

        filepath = None

        if resource['id']:
            filepath = f'{self._output_images}/{resource["id"]}.jpg'
        else:
            filepath = tempfile.NamedTemporaryFile(prefix='basketcase_', suffix='.jpg', dir=self._output_images, delete=False)

        image.save(filepath, format='JPEG')

    def _get_videos(self, urls):
        if self._session.cookies.get('sessionid'):
            # Add the session cookie
            yt_dlp.utils.std_headers.update({'Cookie': 'sessionid=' + self._session.cookies.get('sessionid')})

        ydl_opts = {
            'outtmpl': self._output_videos + '/%(title)s.%(ext)s' # Set output directory
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)


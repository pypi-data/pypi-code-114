# 대용량 파일의 경우 git에 올릴 수 없기 때문에 구글 드라이브에 업로드 되어있는 자료를 바로 받아오도록 함
# reference https://github.com/teddylee777/gdrive_datasets
# reference https://github.com/ndrplz/google-drive-downloader/blob/master/google_drive_downloader/google_drive_downloader.py

from google_drive_downloader import GoogleDriveDownloader as gdd
import urllib.request
import zipfile
import os
import argparse
import zipfile
import warnings
from sys import stdout
from os import makedirs
from os.path import dirname
from os.path import exists
from cpt_list import cpt_list

def download_from_gdrive(file_id=None, cpt_id=None, cpt_name="dacon", folder='data', unzip=True):
    '''
    Args:
        file_id: (str) 구글 드라이브 다운로드 링크 파일 id. 예시: 1RDAVsCCQCs1bxjq_2Q6qPlGeztnQ2AMD
        cpt_id: (str) 대회 id. cpt_list.py 와 연동이 반드시 필요. 
        cpt_name: (str) 대회 이름. 데이터 zip 파일 이름. 이 이름의 폴더 안에 데이터 압축이 풀림.
        folder: (str) 상위 폴더 이름. 여기 안에 cpt_name 별로 데이터가 저장될 것. (./folder/cpt_name/data.csv)
        unzip: (bool) 압축 파일을 풀 지 여부. 기본은 True
    Return:
        zip 파일이 다운로드 되고 압축이 풀림
    '''
    if file_id == None:
        file_id = cpt_list[cpt_id]

    gdd.download_file_from_google_drive(file_id, dest_path=f'{folder}/{cpt_name}.zip', overwrite=True, showsize=True)
    
    if unzip:
        destination_directory = f'{folder}/{cpt_name}'
        if not exists(destination_directory):
            makedirs(destination_directory)
        try:
            print('Unzipping...', end='')
            stdout.flush()
            with zipfile.ZipFile(f'{folder}/{cpt_name}.zip', 'r') as z:
                z.extractall(destination_directory)
            print('Done.')
        except zipfile.BadZipfile:
            warnings.warn(f'Ignoring `unzip` since "{folder}/{cpt_name}.zip" does not look like a valid zip file')
    
# TODO: 확인 필요. mail@dacon.io 접근 권한 없어서 한글 제목 파일 확인 못함.
    # local_zip = 'dataset.zip'
    # unzip(local_zip, folder)

# reference @ https://gldmg.tistory.com/141
# treating Hangul encoding problem
def unzip(source_file, dest_path):
    with zipfile.ZipFile(source_file, 'r') as zf:
        zipInfo = zf.infolist()
        for member in zipInfo:
            try:
                member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')
                zf.extract(member, dest_path)
            except:
                print(source_file)
                raise Exception('unzipping error')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download zip file from G-Drive')
    parser.add_argument('--file-id', type=str, 
                        help='file id from download url. E.g. 1RDAVsCCQCs1bxjq_2Q6qPlGeztnQ2AMD')
    parser.add_argument('--cpt-id', type=str, 
                        help='cpt id. e.g. 235877')                   
    parser.add_argument('--cpt-name', type=str, default='Dacon',
                        help='competition name. Default: Dacon')
    parser.add_argument('--folder', type=str, default='data',
                        help='download folder name. Default: data')
    parser.add_argument('--unzip', type=bool, default='False',
                        help='unzip data. Default: False')
    args = parser.parse_args()
    download_from_gdrive(args.file_id, args.cpt_id, args.cpt_name, args.folder, args.unzip)
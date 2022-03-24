import py7zr
import re


filter_pattern = re.compile(r'logandconfig.zip')
with py7zr.SevenZipFile('C:/Users/rothf9/Downloads/PR-c5800-518-20210119_162040.zip', mode='r', password='secret') as archive:
    allfiles = archive.getnames()
    selective_files = [f for f in allfiles if filter_pattern.match(f)]
    archive.extract(targets=selective_files)
import csv
import io

import chardet


def _uploadedfile_to_stringio(uploaded_file):
    """ UploadedFileオブジェクトを、テキストI/Oとして扱えるようにする """
    charset = 'utf_8'  # DEFAULT
    for data in uploaded_file.chunks():
        detected_charset = chardet.detect(data)
        charset = detected_charset['encoding'].lower().replace('-', '_')
        break
    return io.TextIOWrapper(uploaded_file.open(), encoding=charset)


def read_uploaded_csv(csv_file):
    """ フォームからアップロードされたCSVファイルを読み込む """
    # TODO: CSVフォーマットかの検証をするようにする
    return csv.reader(_uploadedfile_to_stringio(csv_file), strict=True)

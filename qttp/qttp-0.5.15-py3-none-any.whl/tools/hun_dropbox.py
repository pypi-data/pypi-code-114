import dropbox
import pandas as pd
import pickle
import io
import json

class HunDropbox:
    def __init__(self, token):
        self.dbx = dropbox.Dropbox(token)

    def get_file_list(self, path):
        contents = self.dbx.files_list_folder(path)
        files_name = [content.name for content in contents.entries]
        return files_name

    def read_csv_without_index(self, path, csv_name):
        downfile, f = self.dbx.files_download(path+csv_name)
        df = pd.read_csv(f.raw)
        return df

    def read_csv(self, path, csv_name):
        downfile, f = self.dbx.files_download(path+csv_name)
        df = pd.read_csv(f.raw, index_col=['date'])
        df.index = pd.to_datetime(df.index)
        return df

    def save_csv(self, path, csv_name, df):
        df_string = df.to_csv()
        db_bytes = bytes(df_string, 'utf8')
        self.dbx.files_upload(
            f=db_bytes,
            path=path + csv_name,
            mode=dropbox.files.WriteMode.overwrite
        )

    def save_json(self, path, name, data):
        # https://villoro.com/post/dropbox_python 참고
        with io.StringIO() as stream:
            json.dump(data, stream, indent=4)
            stream.seek(0)
            self.dbx.files_upload(
                f    = stream.read().encode(),
                path = path+name,
                mode =dropbox.files.WriteMode.overwrite
            )

    def read_json(self, path, file_name):
        # https://villoro.com/post/dropbox_python 참고
        _, res = self.dbx.files_download(path+file_name)
        with io.BytesIO(res.content) as stream:
            data = json.load(stream)
        return data

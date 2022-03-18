import base64
import datetime
import time
import json
import os
import requests
import click

from cqh_file.utils import get_md5


class ClientLoop(object):
    def __init__(self, url, dir, sleep, delete):
        self.url = url
        self.dir_list = dir
        self.sleep = sleep
        self.delete = delete
        self.session = requests.Session()

    def path_url(self, url_path):
        return "{}/{}".format(self.url, url_path.lstrip("/"))

    def request_url(self, url, **kwargs):
        res = self.session.post(url, **kwargs)
        return res

    def read_serve_list(self, dir):
        url = self.path_url("/list")
        res = self.request_url(url, json={})
        click.echo("dir: [{}],serve, status_code:{} text:{}".format(dir,res.status_code, res.text))
        click.echo("dir:[{}],serve, res:  cost:{}".format(dir,res.elapsed.total_seconds()))
        j = res.json()
        with open(os.path.join(dir, ".serve.json"), 'w', encoding='utf-8') as f:
            f.write(json.dumps(j, ensure_ascii=False, indent=2,sort_keys=True))
        return j
    
    def check_res(self, res, prefix=""):
        status_code = res.status_code
        if status_code != 200:
            raise ValueError("{} status code error {}".format(prefix, status_code))
        

    def read_client_md5_value(self, dir):
        d = {}
        for name in os.listdir(dir):
            file_path = os.path.join(dir, name)
            if os.path.exists(file_path) and os.path.isfile(file_path) and name[0] != ".":
                d[name] = get_md5(file_path)
        with open(os.path.join(dir, ".client.json"), 'w', encoding='utf-8') as f:
            f.write(json.dumps(d, ensure_ascii=False, indent=2, sort_keys=True))
        return d

    def loop(self):
        while 1:
            start = time.time()
            self.run_once()
            end = time.time()
            click.echo("="*80)
            click.echo("download once complete".center(80, " "))
            click.echo("download cost {}".format(round(end-start, 2)))
            click.echo("="*80)
            click.echo("sleep {}, {}".format(self.sleep, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            time.sleep(self.sleep)
    
    def try_delete(self, dir):
        if not self.delete:
            return
        for name in os.listdir(dir):
            file_path = os.path.join(dir, name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                click.echo("delete name: [{}]".format(name))

    def run_once(self):
        for dir in self.dir_list:
            try:
                if not os.path.exists(dir):
                    os.makedirs(dir)
                    click.echo("create dir {}".format(dir))
                self.try_delete(dir)
                j = self.read_serve_list(dir)
                client_d = self.read_client_md5_value(dir)
                # 遍历所有的名字,检查需不需要下载,然后下载就好了
                count = 0
                for name, md5_value in j.items():
                    if name not in client_d:
                        count +=1
                        self.download(name, client_d, dir)
                        continue
                    if client_d[name] != md5_value:
                        count +=1
                        self.download(name, client_d, dir)
                click.echo("[{}],download file count: {}".format(dir, count))
                click.echo("="*80)
                click.echo("[{}] complete".format(dir))
                click.echo("="*80)
                self.read_client_md5_value(dir)
            except Exception as e:
                click.echo("fail to download for dir [{}]".format(dir))
            
    
    def download(self, name,d, dir):
        prefix = "dir:[{}]".format(dir)
        url = self.path_url("/download")
        res = self.request_url(url, json={"name": name})
        click.echo("{}, download name:{}, cost:{}".format(prefix, name, res.elapsed.total_seconds()))
        j = res.json()
        if res.status_code != 200 or j['code']!=0:
            click.echo("{},download error {}".format(prefix, res.status_code, res.text))
            return
        base64_str = j['data']
        raw_data = base64.b64decode(base64_str)
        with open(os.path.join(dir, name), 'wb') as f:
            f.write(raw_data)


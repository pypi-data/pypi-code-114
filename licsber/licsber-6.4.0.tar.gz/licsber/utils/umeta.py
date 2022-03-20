import hashlib
import json
import os


class Meta:
    def __init__(self, filepath, buf_size=4 * 1024 * 1024):
        abspath = os.path.abspath(filepath)
        if not os.path.exists(abspath):
            print(f"文件不存在 请检查: {abspath}")
            raise FileNotFoundError

        self.buf_size = buf_size

        self._meta = {
            'abspath': abspath,
            'basename': os.path.basename(filepath),
            'size': os.path.getsize(filepath),
            'mtime': int(os.path.getmtime(filepath)),
            'sha1': '',
            'md5': '',
            '115_sha1': '',
            'baidu_md5': '',
            'sha256': '',
        }
        self._cal_all()

    @property
    def link_115(self):
        return f"115://{self.basename}|{self.size}|{self.sha1}|{self.head_sha1}"

    @property
    def link_ali(self):
        return f"aliyunpan://{self.basename}|{self.sha1}|{self.size}|TMP[Licsber]"

    @property
    def link_baidu(self):
        return f"{self.md5}#{self.head_md5}#{self.size}#{self.basename}"

    @property
    def csv_header(self):
        return 'Key,Filename,Size,SHA1,HeadSHA1,MD5,HeadMD5\n'

    @property
    def csv(self):
        res = self.csv_header
        res += f"Value,{self.basename},{self.size},{self.sha1},{self.head_sha1},{self.md5},{self.head_md5}\n"
        res += f",,,,,,{self.link_115}\n"
        res += f",,,,,,{self.link_ali}\n"
        res += f",,,,,,{self.link_baidu}"
        return res

    def save_meta_csv(self):
        with open(self.abspath + '.licsber.csv', 'w') as f:
            f.write(self.csv)

    def __str__(self):
        res = self._meta.copy()
        del res['abspath']
        res.update({
            'link_115': self.link_115,
            'link_ali': self.link_ali,
            'link_baidu': self.link_baidu,
        })
        return json.dumps(res, ensure_ascii=False)

    @property
    def abspath(self):
        return self._meta['abspath']

    @property
    def basename(self):
        return self._meta['basename']

    @property
    def size(self):
        return self._meta['size']

    @property
    def mtime(self):
        return self._meta['mtime']

    @property
    def md5(self):
        return self._meta['md5']

    @property
    def sha1(self):
        return self._meta['sha1']

    @property
    def sha256(self):
        return self._meta['sha256']

    @property
    def head_sha1(self):
        return self._meta['115_sha1']

    @property
    def head_md5(self):
        return self._meta['baidu_md5']

    def _cal_all(self):
        with open(self.abspath, 'rb') as f:
            head_sha1_obj = hashlib.sha1()
            num_bytes = 128 * 1024
            content = f.read(num_bytes)
            if (l := len(content)) < num_bytes:
                content += b'\0' * (num_bytes - l)
            head_sha1_obj.update(content)
            self._meta['115_sha1'] = head_sha1_obj.hexdigest().upper()

            f.seek(0)
            head_md5_obj = hashlib.md5()
            num_bytes = 256 * 1024
            content = f.read(num_bytes)
            if (l := len(content)) < num_bytes:
                content += b'\0' * (num_bytes - l)
            head_md5_obj.update(content)
            self._meta['baidu_md5'] = head_md5_obj.hexdigest().upper()

            f.seek(0)
            md5_obj = hashlib.md5()
            sha1_obj = hashlib.sha1()
            sha256_obj = hashlib.sha256()
            while True:
                content = f.read(self.buf_size)
                if not content:
                    break

                md5_obj.update(content)
                sha1_obj.update(content)
                sha256_obj.update(content)

            self._meta['md5'] = md5_obj.hexdigest().upper()
            self._meta['sha1'] = sha1_obj.hexdigest().upper()
            self._meta['sha256'] = sha256_obj.hexdigest().upper()


if __name__ == '__main__':
    test_path = '/tmp/test.licsber'
    with open(test_path, 'w') as f:
        f.write('Hello Licsber.')

    meta = Meta(test_path)
    meta.save_meta_csv()
    print(meta, end='')
    assert meta.link_115 == '115://test.licsber|14|02B02681636CCEDB820385C8A87EA2E1E18ACD5C|C24486ADE0E6AAE9376E4994A7A1267277A13295'

# @Time : 2022/3/13 11:39 AM 
# @Author : SailYang
import yaml


class YamlHelper(object):
    @staticmethod
    def read_yaml(yaml_file_path):
        with open(yaml_file_path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

import subprocess
import toml
import appdirs
import os
import shutil

this_dir = os.path.dirname(__file__)
default_conf = os.path.join(this_dir, 'conf.toml')
conf_dir = appdirs.user_config_dir('lyberry')
conf_file_path = os.path.join(conf_dir, 'conf.toml')
settings = {}

def load():
    user_conf = get_user_conf()
    global settings
    settings = get_conf(default_conf)
    settings.update(user_conf)

def get_user_conf():
    try:
        return get_conf(conf_file_path)
    except FileNotFoundError:
        return {}

def get_conf(path):
    with open(path, 'r') as conf_file:
        conf_text = conf_file.read()
        return toml.loads(conf_text)

def apply():
    global settings
    with open(conf_file_path, 'w') as conf_file:
        conf_file.write(toml.dumps(settings))

load()

def media_player(file):
    run_cmd(settings["player_cmd"], file)

def text_viewer(file):
    run_cmd(settings["viewer_cmd"], file)

def run_cmd(cmd, arg):
    command = cmd.split()
    try:
        i = command.index('{}')
        command.insert(i, arg)
        command.remove('{}')
    except:
        command.append(arg)
    subprocess.run(command)


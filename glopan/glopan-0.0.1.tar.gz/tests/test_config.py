import json

import glopan
from glopan.config import HOMEPATH, CONFIG_FILENAME, Config


def test_init_with_config_file():
    assert isinstance(glopan.config.config, dict)


def test_init_without_config_file():
    # Remove existing config_file and init new Config
    config_file = HOMEPATH / CONFIG_FILENAME
    temp_config = {**glopan.config.config}
    config_file.unlink()
    test_config = Config()
    assert test_config.config == {
        'inkscape_path': None,
        'ps2pdf_path': None,
    }
    # Reset config_file
    with open(config_file, 'w', encoding='utf-8') as outfile:
        json.dump(temp_config, outfile)
    for key, value in temp_config.items():
        glopan.config.set(key, value)


def test_reset_config():
    config_file = HOMEPATH / CONFIG_FILENAME
    with open(config_file, 'r', encoding='utf-8') as infile:
        temp_config = json.load(infile)
    glopan.config.reset()
    assert glopan.config.config == {
        'inkscape_path': None,
        'ps2pdf_path': None,
    }
    # Reset config_file
    with open(config_file, 'w', encoding='utf-8') as outfile:
        json.dump(temp_config, outfile)
    for key, value in temp_config.items():
        glopan.config.set(key, value)


def test_set_config(inkscape_path, ps2pdf_path):
    glopan.config.set('inkscape_path', str(inkscape_path))
    assert glopan.config.config['inkscape_path'] == str(inkscape_path)
    glopan.config.set('ps2pdf_path', str(ps2pdf_path))
    assert glopan.config.config['ps2pdf_path'] == str(ps2pdf_path)


def test_check_config():
    temp_config = {**glopan.config.config}
    assert glopan.config.check_config('inkscape_path') is True
    assert glopan.config.check_config('asdf') is False
    glopan.config.reset()
    assert glopan.config.check_config('inkscape_path') is False
    glopan.config.set('inkscape_path', 'asdf')
    assert glopan.config.check_config('inkscape_path') is False
    for key, value in temp_config.items():
        glopan.config.set(key, value)

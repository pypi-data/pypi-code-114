import os

from mg_file.file.env_file import EnvFile


def test_read():
    r = EnvFile("./data_set/__env.env")
    print(r.readAndSetEnv())
    assert os.environ.get("DEBUG") == "True"
    assert os.environ.get("PORT") == "8080"

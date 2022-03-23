import importlib
import os
import sys
from multiprocessing import Process

import databutton as db
from databutton.helpers import parse
from databutton.server.processes import start_processes
from fastapi import FastAPI

app = FastAPI()

sys.path.append(os.curdir)
imports = parse.find_databutton_directive_modules()
streamlit_modules = {}
for name in imports:
    streamlit_modules[name] = importlib.import_module(name)


@app.on_event('startup')
async def start_servers():
    print('Starting processes')
    await start_processes(app, db._streamlit_apps)

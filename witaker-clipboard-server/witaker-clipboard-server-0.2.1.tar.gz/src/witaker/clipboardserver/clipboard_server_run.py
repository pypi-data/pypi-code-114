from multiprocessing import Process

import eventlet
from eventlet import wsgi

DEFAULT_SERVER_PORT = 42157

def start_flask_webserver(port, app):
    wsgi.server(eventlet.listen(('localhost', port)), app)

def start_server_process(server_port, app):
    server_process = Process(target=start_flask_webserver, args=(server_port, app))
    server_process.start()
    return server_process

def stop_server_process(server_process):
    server_process.terminate()
    server_process.join()
    server_process.close()


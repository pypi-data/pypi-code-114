import os
import signal
import argparse
import ipaddress
import importlib

import bjoern # Does not work for Windows

environ = os.environ

DEFAULT_PORT = 8088

parser = argparse.ArgumentParser(description='Make this baby run on Bjoern')

parser.add_argument('positional', metavar='wsgi_app', nargs='+', help='Path to wsgi application')

parser.add_argument("-w", dest='workers', required=False, type=int, default=int(environ.get('WORKERS', 1)))

parser.add_argument("-p", dest='port', default=environ.get('PORT'), type=int, required=False)

parser.add_argument("-i", dest='host', required=False, default=environ.get('HOST', '127.0.0.1'))

def main():
    args = parser.parse_args()

    if args.workers < 1:
        raise AttributeError(f'Workers must not be less than 1')

    wsgi_module_path = args.positional[0]

    wsgi_module = importlib.import_module(wsgi_module_path)

    app = wsgi_module.get_wsgi_application()

    workers = args.workers

    worker_pids = []

    print(f'Starting Bjoern on {args.host}{f":{args.port}" if args.port else ""}')

    host = args.host

    port = args.port

    if not port:
        try:
            ipaddress.ip_network(host)

            port = DEFAULT_PORT
        except ValueError:
            pass

    bjoern.listen(app, host, port)

    
    print('Bjoern server has started')

    for i in range(workers):
        print(f'Forking worker #{i + 1}')

        pid = os.fork()

        print(f'Forked worker #{i + 1}')

        if pid > 0:
            # in master
            worker_pids.append(pid)
        elif pid == 0:
            # in worker

            try:
                bjoern.run()
            except KeyboardInterrupt:
                pass

            exit()

    try:
        # Wait for the first worker to exit. They should never exit!
        # Once first is dead, kill the others and exit with error code.

        pid, _ = os.wait()

        worker_pids.remove(pid)

    finally:
        for pid in worker_pids:
            os.kill(pid, signal.SIGINT)

            exit(1)


if __name__ == '__main__':
    main()

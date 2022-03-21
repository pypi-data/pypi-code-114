import os

from notebuild.core.core import command_line_parser
from notebuild.manage import BaseServer, ServerManage

# sudo kill -9 `sudo lsof -t -i:5860`
# gunicorn -c gun.py manage:app
# nohup gunicorn -c gun.py manage:app  >>/notechats/logs/notecorn/server-$(date +%Y-%m-%d).log 2>&1 &


class CronServer(BaseServer):
    def __init__(self):
        path = os.path.abspath(os.path.dirname(__file__))
        super(CronServer, self).__init__('notecron_server', path)

    def init(self):
        manage = ServerManage()
        try:
            manage.init()
        except Exception as e:
            print(e)

        manage.add_job(server_name=self.server_name,
                       directory=self.current_path,
                       command="gunicorn -c config.py notecron_server:app",
                       user='bingtao',
                       stdout_logfile="/notechats/logs/notecron/notecron.log")
        manage.start()


def notecron():
    args = command_line_parser()
    package = CronServer()
    if args.command == 'init':
        package.init()
    elif args.command == 'stop':
        package.stop()
    elif args.command == 'start':
        package.start()
    elif args.command == 'restart':
        package.restart()
    elif args.command == 'help':
        info = """
init
stop
start
restart
        """
        print(info)

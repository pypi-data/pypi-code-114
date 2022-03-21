import logging
import os
from optparse import OptionParser
from gevent import pywsgi
from SpiderKeeper.app import app, initialize


def main():
    opts, args = parse_opts(app.config)
    app.config.update(dict(
        SERVER_TYPE=opts.server_type,
        SERVERS=opts.servers or app.config.get('SERVERS'),
        SQLALCHEMY_DATABASE_URI=opts.database_url,
        BASIC_AUTH_USERNAME=opts.username,
        BASIC_AUTH_PASSWORD=opts.password,
        NO_AUTH=opts.no_auth,
        SCRAPYD_BASIC_AUTH_USERNAME=opts.scrapyd_username,
        SCRAPYD_BASIC_AUTH_PASSWORD=opts.scrapyd_password
    ))
    if opts.verbose:
        app.logger.setLevel(logging.DEBUG)
    initialize()
    app.logger.info("SpiderKeeper startd on %s:%s username:%s/password:%s with %s servers:%s" % (
        opts.host, opts.port, opts.username, opts.password, opts.server_type, ','.join(app.config.get('SERVERS', []))))
    # app.run(host=opts.host, port=opts.port, use_reloader=False, threaded=True)
    server = pywsgi.WSGIServer((opts.host, opts.port), app)
    server.serve_forever()


def parse_opts(config):
    parser = OptionParser(usage="%prog [options]",
                          description="Admin ui for spider service")
    parser.add_option("--host",
                      help="host, default:0.0.0.0",
                      dest='host',
                      default='0.0.0.0')
    parser.add_option("--port",
                      help="port, default:5000",
                      dest='port',
                      type="int",
                      default=5000)
    parser.add_option("--username",
                      help="basic auth username ,default: %s" % config.get('BASIC_AUTH_USERNAME'),
                      dest='username',
                      default=config.get('BASIC_AUTH_USERNAME'))
    parser.add_option("--password",
                      help="basic auth password ,default: %s" % config.get('BASIC_AUTH_PASSWORD'),
                      dest='password',
                      default=config.get('BASIC_AUTH_PASSWORD'))
    parser.add_option("--scrapyd_username",
                      help="scrapyd basic auth username ,default: %s" % config.get('SCRAPYD_BASIC_AUTH_USERNAME'),
                      dest='scrapyd_username',
                      default=config.get('SCRAPYD_BASIC_AUTH_USERNAME'))
    parser.add_option("--scrapyd_password",
                      help="scrapyd basic auth password ,default: %s" % config.get('SCRAPYD_BASIC_AUTH_PASSWORD'),
                      dest='scrapyd_password',
                      default=config.get('SCRAPYD_BASIC_AUTH_PASSWORD'))
    parser.add_option("--type",
                      help="access spider server type, default: %s" % config.get('SERVER_TYPE'),
                      dest='server_type',
                      default=config.get('SERVER_TYPE'))
    parser.add_option("--server",
                      help="servers, default: %s" % config.get('SERVERS'),
                      dest='servers',
                      action='append',
                      default=[])
    parser.add_option("--database-url",
                      help='SpiderKeeper metadata database default: %s' % config.get('SQLALCHEMY_DATABASE_URI'),
                      dest='database_url',
                      default=config.get('SQLALCHEMY_DATABASE_URI'))

    parser.add_option("--no-auth",
                      help="disable basic auth",
                      dest='no_auth',
                      action='store_true',
                      default=config.get('NO_AUTH'))
    parser.add_option("-v", "--verbose",
                      help="log level",
                      dest='verbose',
                      action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    main()

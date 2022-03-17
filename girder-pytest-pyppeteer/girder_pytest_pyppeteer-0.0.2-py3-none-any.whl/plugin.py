import os

import logging
import pytest
import re
import shlex
import signal
from subprocess import PIPE, Popen, TimeoutExpired

log = logging.getLogger('pytest-pyppeteer')

def pytest_addoption(parser, pluginmanager):
    parser.addoption(
        "--client-command",
        dest='PYPPETEER_TEST_CLIENT_COMMAND',
        help="The command to start the test client",
        default=os.getenv('PYPPETEER_TEST_CLIENT_COMMAND'),
    )
    parser.addoption(
        "--client-dir",
        dest='PYPPETEER_TEST_CLIENT_DIR',
        help="The directory to start the test client in",
        default=os.getenv('PYPPETEER_TEST_CLIENT_DIR'),
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "pyppeteer: This is a pyppeteer test.")


@pytest.fixture(scope='session')
def _pyppeteer_config(request):
    config = {
        'PYPPETEER_TEST_CLIENT_COMMAND': request.config.getoption('PYPPETEER_TEST_CLIENT_COMMAND'),
        'PYPPETEER_TEST_CLIENT_DIR': request.config.getoption('PYPPETEER_TEST_CLIENT_DIR'),
    }
    for key, value in config.items():
        if value is None:
            pytest.fail(f'{key} not defined')
    return config

@pytest.fixture(scope='session')
def webpack_server(_pyppeteer_config, live_server):
    try:
        import pyppeteer
        import pytest_asyncio
    except ModuleNotFoundError as e:
        pytest.skip(f'{e.name} not found')
    env = {
        'VUE_APP_OAUTH_CLIENT_ID': 'test-oauth-client-id',
        **os.environ,
        'VUE_APP_API_ROOT': f'{live_server.url}/api/v1',
        'VUE_APP_OAUTH_API_ROOT': f'{live_server.url}/oauth/',
    }

    command = ['/usr/bin/env'] + shlex.split(_pyppeteer_config['PYPPETEER_TEST_CLIENT_COMMAND'])
    log.debug(f'Launching node server with {command}')
    process = Popen(
        command,
        cwd=_pyppeteer_config['PYPPETEER_TEST_CLIENT_DIR'],
        env=env,
        stdout=PIPE,
        stderr=PIPE,
        preexec_fn=os.setsid,
    )
    try:
        # Wait until the server starts by polling stdout
        max_timeout = 60
        retry_interval = 3
        err = b''
        for _ in range(0, max_timeout // retry_interval):
            try:
                _out, err = process.communicate(timeout=retry_interval)
            except TimeoutExpired as e:
                if match := re.search(
                    b'App running at:\n  - Local:   (http[s]?://[a-z]+:[0-9]+/?) \n', e.stdout
                ):
                    url = match.group(1).decode('utf-8')
                    break
        else:
            raise Exception(f'webpack server failed to start: {err}')
        yield url
    finally:
        # Kill every process in the webpack server's process group
        try:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            # TODO set up some signal handlers to ensure it always gets cleaned up
        except ProcessLookupError:
            # The process has already terminated, no need to intervene
            pass


@pytest.fixture
async def page():
    try:
        from pyppeteer.launcher import Launcher
        from pyppeteer.errors import BrowserError
        import pytest_asyncio
    except ModuleNotFoundError as e:
        pytest.skip(f'{e.name} not found')
    launch_kwargs = {
        'ignoreHTTPSErrors':True,
        'headless':True,
        'defaultViewport':{'width': 1024, 'height': 800},
        'args': ['--no-sandbox'],
        'dumpio': True,
    }
    launcher = Launcher(**launch_kwargs)
    try:
        browser = await launcher.launch()
    except BrowserError as e:
        launch_command = ' '.join(launcher.cmd)
        log.error(f'The pyppeteer browser failed to launch.')
        log.error(f'You may be able to get more information on the error by starting the browser process yourself:')
        log.error(launch_command)

        raise e
    page = await browser.newPage()

    @page.on('console')
    def _console_log_handler(message):
        log.debug(f'{message.type} {message.args} {message.text}')

    yield page
    await browser.close()


@pytest.fixture
def oauth_application(webpack_server):
    from oauth2_provider.models import get_application_model
    Application = get_application_model()
    application = Application(
        name='test-client-application',
        client_id='test-oauth-client-id', # TODO no magic strings
        client_secret='',
        client_type='public',
        redirect_uris=webpack_server,
        authorization_grant_type='authorization-code',
        skip_authorization=True,
    )
    application.save()
    return application

@pytest.fixture
def page_login(live_server, webpack_server, oauth_application, client):
    async def _page_login(page, user):
        client.force_login(user)
        sessionid = client.cookies['sessionid'].value
        await page.setCookie(
            {
                'name': 'sessionid',
                'value': sessionid,
                'url': live_server.url,
                'path': '/',
            }
        )
        await page.waitFor(2_000) # TODO more reliable wait
    return _page_login
import os

import logging
import pytest
import re
import shlex
import signal
from subprocess import PIPE, Popen, TimeoutExpired

log = logging.getLogger('pytest-pyppeteer')


def pytest_configure(config):
    config.addinivalue_line('markers', 'pyppeteer: This is a pyppeteer test.')


def is_pyppeteer_enabled(request):
    """Determine if the pyppeteer mark was specified when invoking pytest."""
    return 'pyppeteer' in request.config.getoption('markexpr')


def skip_if_pyppeteer_disabled(request):
    """Skip the test if the pyppeteer mark was not specified when invoking pytest"""
    if not is_pyppeteer_enabled(request):
        pytest.skip('pyppeteer mark not specified')

@pytest.fixture(scope='session')
def _pyppeteer_config(request):
    # We cannot use skip_if_pyppeteer_disabled here because this fixture is session scoped.
    # Instead, just don't return anything. Anything that would use this fixture would skip anyway.
    if is_pyppeteer_enabled(request):
        config = {
            # The default configuration
            'VUE_APP_API_ROOT': '{live_server}/api/v1',
            'VUE_APP_OAUTH_API_ROOT': '{live_server}/oauth/',
            'VUE_APP_OAUTH_CLIENT_ID': 'test-oauth-client-id',
            # Any env vars that start with "PYPPETEER_" with the prefix trimmed
            **{
                key[10:]:value
                for (key,value) in os.environ.items()
                if key.startswith('PYPPETEER_')
            },
        }
        required_settings = ['TEST_CLIENT_COMMAND', 'TEST_CLIENT_DIR']
        for required_setting in required_settings:
            if required_setting not in config:
                pytest.fail(f'Required environment variable PYPPETEER_{required_setting} not defined')
        return config

@pytest.fixture(scope='session')
def webpack_server(request, _pyppeteer_config, live_server):
    """Webpack server"""
    skip_if_pyppeteer_disabled(request)
    env = {
        # The path must be passed so that npm/yarn can be found
        **{'PATH': os.getenv('PATH')},
        # Pass everything from the pyppeteer config, formatted for the current environment
        **{
            key:value.format(live_server=live_server.url) for (key, value) in _pyppeteer_config.items()
        },
    }
    command = ['/usr/bin/env'] + shlex.split(_pyppeteer_config['TEST_CLIENT_COMMAND'])
    log.debug(f'Launching node server with {command}')
    process = Popen(
        command,
        cwd=_pyppeteer_config['TEST_CLIENT_DIR'],
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
                match = re.search(
                    b'App running at:\n  - Local:   (http[s]?://[a-z]+:[0-9]+/?) \n', e.stdout
                )
                if match:
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
async def page(request, _pyppeteer_config):
    """
    A pyppeteer page in a fresh browser environment with some sane defaults set.

    Pyppeteer offers a number of arguments to configure the browser during initialization.
    Currently, a subset of these arguments are configurable using environment variables:
    
    Environment Variable|Pyppeteer Equivalent|Values|Default
    ---|---|---|---
    PYPPETEER_BROWSER_IGNORE_HTTPS_ERRORS|ignoreHTTPSErrors|"True"/"1" or "False"/"0"|"True"
    PYPPETEER_BROWSER_HEADLESS|headless|"True"/"1" or "False"/"0"|"True"
    PYPPETEER_BROWSER_WIDTH|defaultViewport.width|int|1024
    PYPPETEER_BROWSER_HEIGHT|defaultViewport.height|int|800
    PYPPETEER_BROWSER_DUMPIO|dumpio|"True"/"1" or "False"/"0"|"True"

    You can set these in your `tox.ini` `setenv` block, or name them in the `passenv` section and set them manually in the shell prior to running tox.
    """
    skip_if_pyppeteer_disabled(request)
    from pyppeteer.launcher import Launcher
    from pyppeteer.errors import BrowserError
    import pytest_asyncio

    launch_kwargs = {
        'ignoreHTTPSErrors': True,
        'headless': True,
        'defaultViewport': {'width': 1024, 'height': 800},
        'args': ['--no-sandbox'],
        'dumpio': True,
    }
    def parse_bool(value):
        if value in ('True', '1'):
            return True
        elif value in ('False', '0'):
            return False
        raise ValueError(f'invalid boolean: \'{value}\'')
    for key, value in _pyppeteer_config.items():
        if key == 'BROWSER_IGNORE_HTTPS_ERRORS':
            launch_kwargs['ignoreHTTPSErrors'] = parse_bool(value)
        if key == 'BROWSER_HEADLESS':
            launch_kwargs['headless'] = parse_bool(value)
        if key == 'BROWSER_WIDTH':
            launch_kwargs['defaultViewport']['width'] = int(value)
        if key == 'BROWSER_HEIGHT':
            launch_kwargs['defaultViewport']['height'] = int(value)
        if key == 'BROWSER_DUMPIO':
            launch_kwargs['dumpio'] = parse_bool(value)

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
def oauth_application(_pyppeteer_config, webpack_server: str):
    from oauth2_provider.models import get_application_model
    Application = get_application_model()
    application = Application(
        name='test-client-application',
        client_id=_pyppeteer_config['VUE_APP_OAUTH_CLIENT_ID'],
        client_secret='',
        client_type='public',
        redirect_uris=webpack_server if webpack_server.endswith('/') else f'{webpack_server}/',
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
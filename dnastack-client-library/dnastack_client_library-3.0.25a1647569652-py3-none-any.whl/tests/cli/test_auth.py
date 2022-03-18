from concurrent.futures import ThreadPoolExecutor

import logging
import re
from imagination import container
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

from .base import CliTestCase
from ..exam_helper import client_id, client_secret, token_endpoint, authorization_endpoint, personal_access_endpoint, \
    redirect_url, device_code_endpoint
from ...helpers.console import Console
from ...helpers.environments import env, flag


class TestAuthentication(CliTestCase):
    re_url = re.compile(r'https://[^\s]+')
    test_resource_url = env('E2E_PROTECTED_DATA_CONNECT_URL', default='https://data-connect-trino.viral.ai/')

    # def log_level(self):
    #     return logging.DEBUG

    def setUp(self) -> None:
        super().setUp()
        self.invoke('config', 'set', 'data_connect.url', self.test_resource_url)

    def test_client_credentials_flow(self):

        self._configure({
            'data_connect.authentication.oauth2.client_id': client_id,
            'data_connect.authentication.oauth2.client_secret': client_secret,
            'data_connect.authentication.oauth2.grant_type': 'client_credentials',
            'data_connect.authentication.oauth2.resource_url': self.test_resource_url,
            'data_connect.authentication.oauth2.token_endpoint': token_endpoint,
        })

        result = self.invoke('auth', 'login', 'data_connect')
        self.assertEqual(0, result.exit_code)

    def test_personal_access_token_flow(self):
        email = env('E2E_AUTH_PAT_TEST_EMAIL')
        token = env('E2E_AUTH_PAT_TEST_TOKEN')

        if not email or not token:
            self.skipTest('The PAT flow test does not have both email and token.')

        self._configure({
            'data_connect.authentication.oauth2.authorization_endpoint': authorization_endpoint,
            'data_connect.authentication.oauth2.client_id': client_id,
            'data_connect.authentication.oauth2.client_secret': client_secret,
            'data_connect.authentication.oauth2.grant_type': 'authorization_code',
            'data_connect.authentication.oauth2.personal_access_endpoint': personal_access_endpoint,
            'data_connect.authentication.oauth2.personal_access_email': email,
            'data_connect.authentication.oauth2.personal_access_token': token,
            'data_connect.authentication.oauth2.redirect_url': redirect_url,
            'data_connect.authentication.oauth2.resource_url': self.test_resource_url,
            'data_connect.authentication.oauth2.token_endpoint': token_endpoint
        })

        result = self.invoke('auth', 'login', 'data_connect')
        self.assertEqual(0, result.exit_code)

    def test_device_code_flow(self):
        email = env('E2E_AUTH_DEVICE_CODE_TEST_EMAIL')
        token = env('E2E_AUTH_DEVICE_CODE_TEST_TOKEN')

        if not email or not token:
            self.skipTest('This test requires both email and personal access token.')

        self._configure({
            'data_connect.authentication.oauth2.client_id': client_id,
            'data_connect.authentication.oauth2.client_secret': client_secret,
            'data_connect.authentication.oauth2.device_code_endpoint': device_code_endpoint,
            'data_connect.authentication.oauth2.grant_type': 'urn:ietf:params:oauth:grant-type:device_code',
            'data_connect.authentication.oauth2.redirect_url': redirect_url,
            'data_connect.authentication.oauth2.resource_url': self.test_resource_url,
            'data_connect.authentication.oauth2.token_endpoint': token_endpoint
        })

        self._logger.debug('Initiating the auth command in a different process...')

        console: Console = container.get(Console)

        with ThreadPoolExecutor() as pool:
            cli_future = pool.submit(self.invoke, 'auth', 'login', 'data_connect', '--no-browser')

            while not cli_future.running():
                pass  # wait for the CLI thread to start

            device_code_url = None
            while device_code_url is None:
                try:
                    output = console.flush_output()

                    matches = TestAuthentication.re_url.search(output)

                    if matches:
                        device_code_url = matches.group(0)
                        self._logger.info('Detected the device code URL')
                    else:
                        self._logger.debug('Waiting...')
                        sleep(1)
                except KeyboardInterrupt:
                    raise RuntimeError('User terminated')

            self._confirm_device_code(device_code_url, email, token)

            self._logger.debug('Waiting for the CLI to join back...')

            result = cli_future.result()

            self.assertEqual(result.exit_code, 0, 'Unexpected exit code')
            self.assertIn("login successful", result.stdout.lower())

    def _confirm_device_code(self, device_code_url, email: str, token: str, allow=True):
        # make sure the browser is opened in headless mode
        chrome_options = Options()
        chrome_options.headless = flag('E2E_HEADLESS')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)

        self._logger.debug(f'Web driver: Activated')

        driver.get(device_code_url)

        self._logger.debug(f'Web driver: Go to {device_code_url}')

        driver.execute_script(
            (
                f"document.querySelector('form[name=\"token\"] input[name=\"token\"]').value = '{token}';"
                f"document.querySelector('form[name=\"token\"] input[name=\"email\"]').value = '{email}';"
            )
        )

        sleep(5)
        self._logger.debug(f'Web driver: Current: URL: {driver.current_url}')
        self._logger.debug(f'Web driver: Current: Source: {driver.page_source}')

        token_form = driver.find_element(By.CSS_SELECTOR, "form[name='token']")
        token_form.submit()

        sleep(2)

        try:
            driver.find_element(By.ID, "continue-btn").click()

            if allow:
                driver.find_element(By.ID, "allow-btn").click()
            else:
                driver.find_element(By.ID, "deny-btn").click()
        finally:
            driver.quit()
            self._logger.debug(f'Web driver: Deactivated')

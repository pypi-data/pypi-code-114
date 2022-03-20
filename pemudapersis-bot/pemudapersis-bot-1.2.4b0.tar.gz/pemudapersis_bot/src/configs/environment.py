""" Configuration """
import logging
import os


class EnvConfig:
    BOT_DB = os.environ.get("BOT_DATABASE")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")
    WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "0.0.0.0")
    WEBHOOK_PORT = os.environ.get("WEBHOOK_PORT", 8443)
    LOG_LEVEL = os.environ.get("BOT_LOG_LEVEL", logging.INFO)
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

    OAUTH_URL = os.environ.get("OAUTH_URL", "http://206.189.147.212:8080/oauth/login")
    OAUTH_CREDS = os.environ.get("OAUTH_CREDS", "YW5hLWNsaWVudDphbmEtc2VjcmV0")
    OAUTH_USERNAME = os.environ.get("OAUTH_USERNAME", "99.0001")
    OAUTH_PASSWORD = os.environ.get("OAUTH_PASSWORD", "12345")
    OAUTH_GRANT_TYPE = os.environ.get("OAUTH_GRANT_TYPE", "password")
    API_ENDPOINT = os.environ.get("API_ENDPOINT", "http://206.189.147.212:8080")

import requests
from datomizer.utils import constants


def get_domain_by_username(username: str) -> str:
    response = requests.get(constants.ONBOARDING_GET_USER_DOMAIN_DEFAULT % username)
    return response.url.replace("https://", "").split('/')[0]


def get_realm_by_domain(domain: str) -> str:
    response = requests.get(constants.IDENTITY_GET_REALM_BY_DOMAIN % domain)
    return response.text


def get_token(username, password, realm, domain):
    client_props = {
        "client_id": "direct",
        "grant_type": "password",
        "username": username,
        "password": password
    }

    response = requests.post(constants.KEYCLOAK_GET_TOKEN_URL % (domain, realm), client_props)
    return response.json()


def refresh_token(realm, domain, token):
    client_props = {
        "client_id": "direct",
        "grant_type": "refresh_token",
        "refresh_token": token
    }

    response = requests.post(constants.KEYCLOAK_GET_TOKEN_URL % (domain, realm), client_props)
    return response.json()


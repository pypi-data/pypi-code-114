"""
`embedops_authorization_test`
=======================================================================
Unit tests for the authorization retrival and storage for EmbedOps 
* Author(s): Bailey Steinfadt
"""

import os

from embedops_cli import embedops_authorization


def test_set_and_get_auth_token():
    """testing setting token"""
    test_secret = "SUPER_DUPER_SECRET_TOKEN_SAUCE"
    test_secret_file = ".test_eosecrets.toml"

    embedops_authorization.set_auth_token(test_secret, test_secret_file)
    retrieved_secret = embedops_authorization.get_auth_token(test_secret_file)

    assert test_secret == retrieved_secret

    os.remove(test_secret_file)


def test_set_and_get_registry_token():
    """testing setting token"""
    test_secret = "YULE NEFFER GESS WOT"
    test_secret_file = ".test_eosecrets.toml"

    embedops_authorization.set_registry_token(test_secret, test_secret_file)
    retrieved_secret = embedops_authorization.get_registry_token(test_secret_file)

    assert test_secret == retrieved_secret

    os.remove(test_secret_file)


def test_setting_both_tokens():
    """Test that both the registry token and auth token can be read and written together"""

    auth_secret = "SUPER_DUPER_SECRET_TOKN_SAUCE"
    other_auth_secret = "THIS IS THE GOOD ONE"
    registry_secret = "YULE NEFFER GESS WOT"

    test_secret_file = ".test_eosecrets.toml"

    embedops_authorization.set_auth_token(auth_secret, test_secret_file)
    embedops_authorization.set_registry_token(registry_secret, test_secret_file)

    read_auth_token = embedops_authorization.get_auth_token(test_secret_file)
    read_registry_token = embedops_authorization.get_registry_token(test_secret_file)

    assert auth_secret == read_auth_token
    assert registry_secret == read_registry_token

    embedops_authorization.set_auth_token(other_auth_secret, test_secret_file)
    read_auth_token = embedops_authorization.get_auth_token(test_secret_file)
    read_registry_token = embedops_authorization.get_registry_token(test_secret_file)

    assert other_auth_secret == read_auth_token
    assert registry_secret == read_registry_token

    os.remove(test_secret_file)

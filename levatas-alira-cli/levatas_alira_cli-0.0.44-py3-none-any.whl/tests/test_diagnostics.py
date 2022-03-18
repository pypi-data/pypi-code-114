import io
import os

from levatas_alira_cli.diagnostics import Diagnostics


def test_multiple_diagnostics():
    configuration = io.StringIO(
        """
    diagnostics:
    - function: levatas_alira_cli.diagnostics.connectivity
      label: Internet connection 1
      endpoint: 8.8.8.8

    - function: levatas_alira_cli.diagnostics.connectivity
      label: Internet connection 2
      endpoint: 0.0.0.0
    """
    )

    result = Diagnostics(configuration=configuration).run()
    assert len(result) == 2
    assert result[0]["status"] is True
    assert result[1]["status"] is False


def test_connectivity_okay():
    configuration = io.StringIO(
        """
    diagnostics:
    - function: levatas_alira_cli.diagnostics.connectivity
      label: Internet connection
      endpoint: 8.8.8.8
    """
    )

    result = Diagnostics(configuration=configuration).run()
    assert result[0]["status"] is True


def test_connectivity_failed():
    configuration = io.StringIO(
        """
    diagnostics:
    - function: levatas_alira_cli.diagnostics.connectivity
      label: Internet connection
      endpoint: 0.0.0.0
    """
    )

    result = Diagnostics(configuration=configuration).run()
    assert result[0]["status"] is False


def test_connectivity_with_http_url():
    configuration = io.StringIO(
        """
    diagnostics:
    - function: levatas_alira_cli.diagnostics.connectivity
      label: Internet connection
      endpoint: http://levatas.com
    """
    )

    result = Diagnostics(configuration=configuration).run()
    assert result[0]["status"] is True


def test_parameters_support_env_references():
    os.environ["ENV_VAR1"] = "0.0.0.0"
    os.environ["ENV_VAR2"] = "8.8.8.8"

    configuration = io.StringIO(
        """
    diagnostics:
    - function: levatas_alira_cli.diagnostics.connectivity
      label: Internet connection
      endpoint: $ENV_VAR1
    - function: levatas_alira_cli.diagnostics.connectivity
      label: Internet connection
      endpoint: $ENV_VAR2
    """
    )

    result = Diagnostics(configuration=configuration).run()
    assert result[0]["status"] is False
    assert result[1]["status"] is True


def test_supports_empty_configuration():
    configuration = io.StringIO(
        """
      """
    )

    result = Diagnostics(configuration=configuration).run()
    assert result == []


def test_supports_no_modules():
    configuration = io.StringIO(
        """
    diagnostics:
    # - function: levatas_alira_cli.diagnostics.connectivity
    #   label: Internet connection
    #   endpoint: $ENV_VAR1
      """
    )

    result = Diagnostics(configuration=configuration).run()
    assert result == []

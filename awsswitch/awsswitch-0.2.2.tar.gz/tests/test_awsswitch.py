"""AWS profile switcher tests."""
import awsswitch


def test_profile_reader(tmp_path):
    """Test profile reader."""
    fake_get_path_called = 0

    def fake_get_path():
        nonlocal fake_get_path_called
        fake_get_path_called += 1
        return tmp_path

    aws_config_file = tmp_path / "config"
    with open("fixtures/aws_config_sample", encoding="utf-8") as file:
        aws_config_file.write_text(file.read())

    assert awsswitch.profile_reader(fake_get_path()) == sorted(
        ["default", "work", "personal"]
    )

    assert fake_get_path_called == 1


def test_awsswitch_select_profile(monkeypatch, tmp_path, capsys):
    """Test awsswitch profile selection."""
    fake_get_path_called = 0

    def fake_get_path():
        nonlocal fake_get_path_called
        fake_get_path_called += 1
        return tmp_path

    monkeypatch.setattr(awsswitch, "get_path", fake_get_path)
    aws_config_file = tmp_path / "config"
    with open("fixtures/aws_config_sample", encoding="utf-8") as file:
        aws_config_file.write_text(file.read())

    def fake_prompt(*args):
        return "work"

    monkeypatch.setattr("awsswitch.prompt", fake_prompt)

    awsswitch.app()

    assert fake_get_path_called == 1

    captured = capsys.readouterr()
    output = captured.out.split("\n")
    assert len(output) == 2
    assert output[0] == "AWS profile switcher"
    assert output[1] == ""


def test_profile_reader_no_aws_config_path(monkeypatch, tmp_path, capsys):
    """Test profile reader without aws config path."""
    fake_get_path_called = 0

    def fake_get_path():
        nonlocal fake_get_path_called
        fake_get_path_called += 1
        return tmp_path / "does_not_exist"

    monkeypatch.setattr(awsswitch, "get_path", fake_get_path)

    awsswitch.app()

    assert fake_get_path_called == 1

    captured = capsys.readouterr()
    output = captured.out.split("\n")
    assert output[0] == "AWS profile switcher"

    err = captured.err.split("\n")
    assert err[0] == "No AWS config path found."


def test_profile_reader_no_aws_config(monkeypatch, tmp_path, capsys):
    """Test profile reader without aws config file."""
    fake_get_path_called = 0

    def fake_get_path():
        nonlocal fake_get_path_called
        fake_get_path_called += 1
        return tmp_path

    monkeypatch.setattr(awsswitch, "get_path", fake_get_path)

    awsswitch.app()

    assert fake_get_path_called == 1

    captured = capsys.readouterr()
    output = captured.out.split("\n")
    assert output[0] == "AWS profile switcher"

    err = captured.err.split("\n")
    assert err[0] == "AWS config path does not exist."

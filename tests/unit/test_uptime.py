from io import StringIO

from sysinfo.uptime import GetUptimeErrors, get_uptime


def test_get_uptime_returns_float():
    uptime = get_uptime()
    assert isinstance(uptime, float)


def generate_mock_open(error: type[FileNotFoundError | ValueError]):
    def mock_open_file_error(*args, **kwargs):
        raise FileNotFoundError

    def mock_open_value_error(*args, **kwargs):
        return StringIO("not-a-number 12345.67")

    if error == FileNotFoundError:
        return mock_open_file_error
    elif error == ValueError:
        return mock_open_value_error


def test_get_uptime_when_file_does_not_exist(monkeypatch):
    monkeypatch.setattr("builtins.open", generate_mock_open(FileNotFoundError))

    expected_error = get_uptime()
    assert expected_error == GetUptimeErrors.FILE_NOT_FOUND


def test_get_uptime_with_invalid_content(monkeypatch):
    monkeypatch.setattr("builtins.open", generate_mock_open(ValueError))

    expected_error = get_uptime()
    assert expected_error == GetUptimeErrors.INVALID_FORMAT

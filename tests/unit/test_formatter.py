from sysinfo.formatter import SystemInfo, format_data, format_output, format_uptime


def test_uptime_formatter_with_none():
    uptime = None
    formatted = format_uptime(uptime)

    assert formatted == "Sorry, We can't provide the updatime data as of now"


def test_uptime_formatter_with_second():
    uptime = 1.0
    formatted = format_uptime(uptime)

    assert formatted == "Uptime: 1 second"


def test_uptime_formatter_with_seconds():
    uptime = 45.0
    formatted = format_uptime(uptime)

    assert formatted == "Uptime: 45 seconds"


def test_uptime_formatter_with_minutes_and_seconds():
    uptime = 125.0  # 2 minutes and 5 seconds
    formatted = format_uptime(uptime)

    assert formatted == "Uptime: 2 minutes, 5 seconds"


def test_uptime_formatter_with_hours_minutes_seconds():
    uptime = 3665.0  # 1 hour, 1 minute, and 5 seconds
    formatted = format_uptime(uptime)

    assert formatted == "Uptime: 1 hour, 1 minute, 5 seconds"


def test_uptime_formatter_with_days_hours_minutes_seconds():
    uptime = 90065.0  # 1 day, 1 hour, 1 minute, and 5 seconds
    formatted = format_uptime(uptime)

    assert formatted == "Uptime: 1 day, 1 hour, 1 minute, 5 seconds"


def test_uptime_formatter_with_plural_units():
    uptime = 172805.0  # 2 days, 0 hours, 0 minutes, and 5 seconds
    formatted = format_uptime(uptime)

    assert formatted == "Uptime: 2 days, 0 hours, 0 minutes, 5 seconds"


def test_format_output():
    uptime = 172805.0  # 2 days, 0 hours, 0 minutes, and 5 seconds
    formatted = format_output(format_data(SystemInfo(uptime=uptime)))

    expected = (
        "\nSystem Information"
        "\n------------------\n"
        "\nUptime: 2 days, 0 hours, 0 minutes, 5 seconds\n"
    )
    assert formatted == expected

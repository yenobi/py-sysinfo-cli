from sysinfo.cli import main


def test_cli_prints_sysinfo(capsys):
    main()

    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()
    header = lines[0]
    divider = lines[1]
    # there is an empty line between the divider and the uptime line, so we need to get the uptime line from index 3
    uptime_line = lines[3]

    assert header == "System Information"
    assert divider == "------------------"
    assert uptime_line.startswith("Uptime: ")

    # validate that nothing was printed to stderr
    assert captured.err == ""

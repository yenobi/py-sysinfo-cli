from sysinfo.cli import main


def test_cli_prints_sysinfo(capsys):
    main()

    captured = capsys.readouterr()

    # print adds a newline character at the end of the output by default
    assert captured.out == "sysinfo\n"
    # validate that nothing was printed to stderr
    assert captured.err == ""

# question: why is import in such format? can i import from the file or only from the module?
# and the next question is won't such format leak the api of the module as public one?
from sysinfo.formatter import SystemInfo, format_data, format_output
from sysinfo.uptime import get_uptime


def collect_data() -> SystemInfo:
    return SystemInfo(uptime=get_uptime())


def main() -> None:
    # args = parse_args()

    data = collect_data()
    formatted_data = format_data(data)
    output = format_output(formatted_data)

    print(output)
    # print("sysinfo")

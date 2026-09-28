from enum import StrEnum


# this was used in first iteration of the code, think about removing it completely
class GetUptimeErrors(StrEnum):
    FILE_NOT_FOUND = "Cannot find `/proc/uptime`"
    INVALID_FORMAT = "Unexpected uptime format"


def get_uptime() -> float | None:
    try:
        with open("/proc/uptime", "r") as file:
            uptime_seconds = float(file.readline().split()[0])
            return uptime_seconds

    except FileNotFoundError, ValueError:
        return None

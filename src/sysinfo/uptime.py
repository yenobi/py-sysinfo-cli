from enum import StrEnum


class GetUptimeErrors(StrEnum):
    FILE_NOT_FOUND = "Cannot find /proc/uptime"
    INVALID_FORMAT = "Unexpected uptime format"


def get_uptime() -> float | str:
    try:
        with open("/proc/uptime", "r") as file:
            uptime_seconds = float(file.readline().split()[0])
            return uptime_seconds

    except FileNotFoundError:
        return GetUptimeErrors.FILE_NOT_FOUND

    except ValueError:
        return GetUptimeErrors.INVALID_FORMAT

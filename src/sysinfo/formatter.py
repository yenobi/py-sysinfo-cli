from dataclasses import dataclass

# @dataclass
# class MemoryInfo:
#     total: int
#     available: int


# @dataclass
# class CpuInfo:
#     model: str
#     cores: int


@dataclass
class SystemInfo:
    uptime: float | None
    # memory: MemoryInfo
    # cpu: CpuInfo


@dataclass
class RenderSystemInfo:
    uptime: str


MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24


# todo: handle `2 days with 0 hours, 0 minutes, and 5 seconds` case
def format_uptime(uptime: float | None) -> str:
    uptime_error_placeholder = "Sorry, We can't provide the updatime data as of now"

    if uptime is None:
        return uptime_error_placeholder

    total_seconds = int(uptime)
    upminutes, upseconds = divmod(total_seconds, MINUTES_IN_HOUR)

    def plural(value: int, unit: str) -> str:
        return unit if value == 1 else f"{unit}s"

    if upminutes == 0:
        return f"Uptime: {upseconds} {plural(upseconds, 'second')}"

    if upminutes < MINUTES_IN_HOUR:
        return f"Uptime: {upminutes} {plural(upminutes, 'minute')}, {upseconds} {plural(upseconds, 'second')}"

    uphours, upminutes = divmod(upminutes, MINUTES_IN_HOUR)

    if uphours < HOURS_IN_DAY:
        return f"Uptime: {uphours} {plural(uphours, 'hour')}, {upminutes} {plural(upminutes, 'minute')}, {upseconds} {plural(upseconds, 'second')}"

    updays, uphours = divmod(uphours, HOURS_IN_DAY)
    return f"Uptime: {updays} {plural(updays, 'day')}, {uphours} {plural(uphours, 'hour')}, {upminutes} {plural(upminutes, 'minute')}, {upseconds} {plural(upseconds, 'second')}"


def format_data(data: SystemInfo) -> RenderSystemInfo:
    return RenderSystemInfo(uptime=format_uptime(data.uptime))


def format_output(data: RenderSystemInfo) -> str:
    header = "\nSystem Information"
    divider = "------------------\n"

    lines = [header, divider]

    if data.uptime:
        lines.append(f"{data.uptime}\n")

    return "\n".join(lines)

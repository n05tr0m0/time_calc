#!/usr/bin/env python3
# # # # # # # # # # # # # # # # # # # # # # # #
# Simple python script for calculating time   #
# by n05tr0m0                                 #
# # # # # # # # # # # # # # # # # # # # # # # #

import argparse
import re
import sys
import time
from datetime import timedelta
from enum import Enum


class TimeFormatEnum(str, Enum):
    HH_MM = '%H:%M'
    HH_MM_SS = '%H:%M:%S'

    def __str__(self) -> str:
        return str.__str__(self)


def convert_to_human_readable_time(input_time: float) -> str:
    if not isinstance(input_time, float):
        return ''
    input_time = input_time % (24 * 3600)
    hour = input_time // 3600
    input_time %= 3600
    minute = input_time // 60
    input_time %= 60
    second = input_time
    return f"{hour:.0f} hour(s), {minute:.0f} minute(s), {second:.0f} second(s)"


def time_to_sec(input_time: str, time_format: str) -> float:
    st = time.strptime(input_time, time_format)
    return timedelta(hours=st.tm_hour, minutes=st.tm_min, seconds=st.tm_sec).total_seconds()


def validate_input(input_string: str) -> float:
    error_msg = 'Incorrect time format. Type -h for help.'
    if re.match(r'^(?:\d|[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)$', input_string):
        return time_to_sec(input_string, TimeFormatEnum.HH_MM_SS)
    if re.match(r'^(?:\d|[01]\d|2[0-3]):[0-5]\d$', input_string):
        return time_to_sec(input_string, TimeFormatEnum.HH_MM)
    print(error_msg)
    sys.exit(1)


def calculating_time():
    program_description = """
    Welcome to the console time calculator.\n
    To calculate the time, enter the start time and the end time of the action or event.\n
    """
    epilog_msg = """
    Use 24-hour format of time.\n
    HH:MM or HH:MM:SS
    """
    parser = argparse.ArgumentParser(
        prog='time_calc',
        description=program_description,
        epilog=epilog_msg,
        exit_on_error=True,
    )
    parser.add_argument('begin', type=str, help='Set the time when event or action started.')
    parser.add_argument('end', type=str, help='Set the time when event or action ended.')
    args = parser.parse_args()

    time_end = validate_input(args.end)
    time_begin = validate_input(args.begin)

    if time_begin > time_end:
        print('The end time must not be earlier than the begin time')
        sys.exit(1)

    result_time = time_end - time_begin
    hr_time_result = convert_to_human_readable_time(result_time)
    print(f'Result time: {hr_time_result}')


if __name__ == '__main__':
    calculating_time()

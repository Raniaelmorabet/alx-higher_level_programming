#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys

def print_stats(total_size, status_codes):
    """
    Prints the statistics based on the given total file size and status codes dictionary.
    """
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

line_count = 0
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        line_count += 1
        split_line = line.split()
        if len(split_line) >= 2:
            status_code = split_line[-2]
            file_size = split_line[-1]
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += int(file_size)

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

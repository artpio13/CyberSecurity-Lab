#!/usr/bin/env python3

import re
import sys

patterns = {
    "sql_injection": re.compile(r"(\\'|--|OR 1=1|SELECT|UNION)", re.IGNORECASE),
    "xss": re.compile(r"(<script>|%3Cscript%3E)", re.IGNORECASE),
    "command_injection": re.compile(r"(;|&&|\\|\\|)", re.IGNORECASE),
    "failed_login": re.compile(r"Failed password", re.IGNORECASE)
}

def scan_log(file_path):
    results = {key: 0 for key in patterns}

    with open(file_path, "r", errors="ignore") as file:
        for line in file:
            for name, pattern in patterns.items():
                if pattern.search(line):
                    results[name] += 1

    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 log_scanner.py <logfile>")
        exit(1)

    logfile = sys.argv[1]
    results = scan_log(logfile)

    print("=== WYNIKI SKANOWANIA ===")
    for key, value in results.items():
        print(f"{key}: {value}")

if results["sql_injection"] > 0:
    print("🚨 ALERT: SQL Injection detected!")

if results["xss"] > 0:
    print("🚨 ALERT: XSS detected!")

if results["command_injection"] > 0:
    print("🚨 ALERT: Command Injection detected!")


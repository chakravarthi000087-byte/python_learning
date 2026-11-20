# Lab Exercise 1: Log file reader program
import os

LOG_FILE = "app.log"

SAMPLE_LOG = """2026-11-01 09:00:01 INFO Server started
2026-11-01 09:05:12 INFO User login: asha
2026-11-01 09:10:45 WARNING Disk usage at 85%
2026-11-01 09:15:30 ERROR Database connection failed
2026-11-01 09:20:00 INFO User login: ravi
2026-11-01 09:25:10 ERROR File not found: report.pdf
2026-11-01 09:30:00 DEBUG Cache cleared
2026-11-01 09:35:22 WARNING Memory usage high
"""


def create_sample_log():
    with open(LOG_FILE, "w") as f:
        f.write(SAMPLE_LOG)
    print(f"Sample log file '{LOG_FILE}' created.")


def read_all():
    with open(LOG_FILE, "r") as f:
        print(f.read())


def filter_by_level(level):
    with open(LOG_FILE, "r") as f:
        matches = [line.strip() for line in f if level in line.split()]
    if matches:
        print("\n".join(matches))
    print(f"\n{len(matches)} {level} entries found.")


def search_keyword(keyword):
    with open(LOG_FILE, "r") as f:
        matches = [f"Line {i}: {line.strip()}" for i, line in enumerate(f, 1)
                   if keyword.lower() in line.lower()]
    if matches:
        print("\n".join(matches))
    print(f"\n{len(matches)} matching lines found.")


def summary():
    levels = {}
    with open(LOG_FILE, "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 3:
                levels[parts[2]] = levels.get(parts[2], 0) + 1
    print(f"Total log entries: {sum(levels.values())}")
    for level, count in levels.items():
        print(f"  {level:<10}{count}")


if not os.path.exists(LOG_FILE):
    print(f"'{LOG_FILE}' not found.")
    create_sample_log()

while True:
    print("\n===== LOG FILE READER =====\n1. Show full log\n2. Filter by level (INFO/WARNING/ERROR/DEBUG)\n3. Search keyword\n4. Summary\n5. Exit")
    ch = input("Enter your choice: ")
    try:
        if ch == "1":
            read_all()
        elif ch == "2":
            filter_by_level(input("Enter level: ").strip().upper())
        elif ch == "3":
            search_keyword(input("Enter keyword: ").strip())
        elif ch == "4":
            summary()
        elif ch == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")
    except FileNotFoundError:
        print("Log file not found.")
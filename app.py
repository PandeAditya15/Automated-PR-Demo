import os
import sqlite3
import subprocess

API_KEY = "sk-demo-1234567890"  # hardcoded secret


def average(nums):
    return sum(nums) / len(nums)  # crashes on empty list


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # SQL injection: user input is formatted straight into the query
    cur.execute(f"SELECT * FROM users WHERE name = '{username}'")
    return cur.fetchone()  # connection is never closed


def run_command(cmd):
    # command injection: shell=True with unsanitised input
    return subprocess.check_output(cmd, shell=True)


def read_config(path):
    try:
        with open(path) as f:
            return f.read()
    except:  # bare except swallows every error
        return None


def divide(a, b):
    return a / b  # no zero check


def find_max(items):
    max_val = 0  # wrong for lists of negative numbers
    for i in items:
        if i > max_val:
            max_val = i
    return max_val


if __name__ == "__main__":
    print(average([]))
    print(os.environ["HOME"])

# File operations are one of the most common uses of context managers.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Don't forget to subscribe to ArjanCodes ;).

# Context managers can help manage external connections like databases, ensuring they close properly.

import sqlite3

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO users (id, name) VALUES (1, 'Alice')")
    conn.commit()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
# The connection is automatically closed at the end of the block.

# [(1, 'Alice'), (1, 'Alice'), (1, 'Alice')]

# You can create your own context manager using generators with @contextmanager.

import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed time: {end - start:.2f} seconds")


# Usage:
with timer():
    total = sum(range(10_000_000))
    print(f"Sum computed: {total}")

# Sum computed: 49999995000000
# Elapsed time: 0.13 seconds

# For more complex scenarios, implement the __enter__ and __exit__ methods directly in a class.


class CustomResource:
    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")


with CustomResource() as resource:
    print("Using the resource")

# Resource acquired
# Using the resource
# Resource released

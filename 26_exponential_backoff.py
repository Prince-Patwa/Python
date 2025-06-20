# Implement an exponential backoff strategy that doubles the wait time b/w retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_tries = 5
attempts = 0

while attempts < max_tries:
    print(f"Attempt {attempts + 1} wait time {wait_time}")
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2
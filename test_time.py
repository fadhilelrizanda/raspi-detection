import time


start_time = time.time()
while True:
    current_time = time.time()
    print(f"Start time {start_time}")
    print(f"current time {current_time-start_time}")
    time.sleep(1)

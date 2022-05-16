import time
import sys
while True:
    try:
        i = input("input: ")
        print("while")
        if i == "stop":
            break
        time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "Its been an hour my Lord",
            timeout = 10
        )
        time.sleep(3600)

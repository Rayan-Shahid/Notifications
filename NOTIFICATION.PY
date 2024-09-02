import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Drink Water",
            message = "Its been an Hour!",
            timeout = 10
        )
        time.sleep(3600)
from datetime import datetime


def get_timestamp():
    # current date and time
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    print("timestamp =", timestamp)
    return timestamp

from datetime import datetime, timedelta


"""
calculate datetime before one day
"""
def get_yesterday():
    now = datetime.now()
    before_one_day = now - timedelta(days = 1)
    return before_one_day


def get_now():
    return datetime.now()

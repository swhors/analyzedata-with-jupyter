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


def get_n_month_before(n: int) -> datetime:
    return datetime.now() - timedelta(days=n*30)


def get_before_ndays(n: int) -> datetime:
    pre_ndays = datetime.now() - timedelta(days=n+1)
    cur_ndays = datetime.now() - timedelta(days=n)

    return pre_ndays, cur_ndays

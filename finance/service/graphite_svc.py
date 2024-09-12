import socket
from _thread import *
from datetime import datetime
from model.market_value import MarketValue


def date_2_datetime(_date):
    args = _date.timetuple()[:6]
    return datetime(*args)


def send_metric(market_value: MarketValue):
    HOST = 'localhost' ## server에 출력되는 ip를 입력해주세요 ##
    PORT = 2003
    dt = date_2_datetime(market_value.updated)
    metric = f'finance.open.{market_value.code} {market_value.open_v} {int(dt.timestamp())}'
    print(f'metric = {metric}')
    try:
        with socket.socket() as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.send(metric.encode('utf-8'))
            client_socket.close()
    except Exception as e:
        print(e)

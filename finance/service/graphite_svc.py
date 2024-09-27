import socket
from _thread import *
from datetime import datetime, timedelta
from model.market_value import MarketValue


def date_2_datetime(_date):
    args = _date.timetuple()[:6]
    return datetime(*args) + timedelta(hours=1)


"""
| code   | varchar(10) | YES  |     | NULL    |                |
| open   | int(11)     | YES  |     | NULL    |                |
| high   | int(11)     | YES  |     | NULL    |                |
| low    | int(11)     | YES  |     | NULL    |                |
| close  | int(11)     | YES  |     | NULL    |                |
| volume | int(11)     | YES  |     | NULL    |                |
| change 
"""
def send_metric(market_value: MarketValue):
    HOST = 'localhost' ## server에 출력되는 ip를 입력해주세요 ##
    PORT = 2003
    dt = date_2_datetime(market_value.updated)
    metric = []
    metric.append(f'finance._{market_value.code}_.open {market_value.open_v}.0 {int(dt.timestamp())}')
    metric.append(f'finance._{market_value.code}_.high {market_value.high}.0 {int(dt.timestamp())}')
    metric.append(f'finance._{market_value.code}_.low {market_value.low}.0 {int(dt.timestamp())}')
    metric.append(f'finance._{market_value.code}_.close {market_value.close}.0 {int(dt.timestamp())}')
    metric.append(f'finance._{market_value.code}_.volume {market_value.volume}.0 {int(dt.timestamp())}')
    metric.append(f'finance._{market_value.code}_.change {market_value.change} {int(dt.timestamp())}\n')
    metrics = "\n".join(metric)
    print(f'metric = {metrics}')
    try:
        with socket.socket() as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.send(metrics.encode('utf-8'))
            client_socket.close()
    except Exception as e:
        print(e)

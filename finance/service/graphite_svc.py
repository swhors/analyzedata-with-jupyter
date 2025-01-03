"""
그라파이트 매트릭 전송을 위한 함수를 정의합니다.
"""
import socket
from _thread import *
from datetime import datetime, timedelta
from model.market_value import MarketValue
import pickle
import struct
import time

DELAY = 1


def date_2_datetime(_date):
    """date를 datetime 형태로 변경합니다."""
    args = _date.timetuple()[:6]
    return datetime(*args) + timedelta(hours=1)


def send_metric(market_value: MarketValue, market="NASDAQ", debug=False):
    """
    매트릭을 전송합니다.
    """
    HOST = 'localhost' ## server에 출력되는 ip를 입력해주세요 ##
    PORT = 2003
    dt = date_2_datetime(market_value.updated).timestamp()
    metrics = []
    metrics.append("finance.%s.%s.open %f %d" % (market, market_value.code, market_value.open_v, dt))
    metrics.append("finance.%s.%s.high %f %d" % (market, market_value.code, market_value.high, dt))
    metrics.append("finance.%s.%s.low %f %d" % (market, market_value.code, market_value.low, dt))
    metrics.append("finance.%s.%s.close %f %d" % (market, market_value.code, market_value.close, dt))
    metrics.append("finance.%s.%s.volume %d %d" % (market, market_value.code, market_value.volume, dt))
    metrics.append("finance.%s.%s.change %f %d" % (market, market_value.code, market_value.change, dt))
    metrics_str = '\n'.join(metrics) + '\n'
    try:
        with socket.socket() as client_socket:
            client_socket.connect((HOST, PORT))
            # client_socket.sendall(metrics_str.encode('utf-8')
            client_socket.sendall(bytes(metrics_str, 'utf-8'))
            # client_socket.close()
    except Exception as e:
        print(e)

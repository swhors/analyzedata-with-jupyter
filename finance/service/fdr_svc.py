import FinanceDataReader as fdr
from datetime import datetime, timedelta
from model.wanted_com import WantedCom
from model.market_value import MarketValue


def get_stock_info(coms_list, from_date: datetime, end_date: datetime):
    """
    get stock information
    """
    infos = []
    for com in coms_list:
        begin = from_date;
        index = 0
        df = fdr.DataReader(com.code, from_date, end_date)
        dates = list(df.index)
        info_dict = df.to_dict('records')
        for value in info_dict:
            market_value = MarketValue.from_dict(value=value, code=com.code, updated=dates[index])
            infos.append(market_value)
            index += 1
    return infos


def get_stock_info_withdatestr(coms_list, from_date: str, end_date: str):
    """
    get stock information
    """
    infos = []
    for com in coms_list:
        begin = from_date;
        index = 0
        df = fdr.DataReader(com.code, from_date, end_date)
        dates = list(df.index)
        info_dict = df.to_dict('records')
        for value in info_dict:
            market_value = MarketValue.from_dict(value=value, code=com.code, updated=dates[index])
            infos.append(market_value)
            index += 1
    return infos

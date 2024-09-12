import FinanceDataReader as fdr
from datetime import datetime, timedelta
from model.wanted_com import WantedCom
from model.market_value import MarketValue


"""
get stock information
"""
def get_stock_info(coms_list, from_date: datetime, end_date: datetime):
    infos = []
    
    for com in coms_list:
        begin = from_date;
        df = fdr.DataReader(com.code, from_date, end_date)
        info_dict = df.to_dict('records')
        for value in info_dict:
            market_value = MarketValue.from_dict(value=value, code=com.code, updated=begin.date())
            infos.append(market_value)
            begin = begin + timedelta(days=1)
    
    return infos

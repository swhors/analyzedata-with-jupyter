class Stock:
    stype: str
    code: str
    name: str
    market: str
    sector: str
    industry: str
    listing_date: str
    settle_month: str
    memo: str

    def __init__(self,
                 stype: str,
                 code: str,
                 name: str,
                 market: str,
                 sector: str,
                 industry: str,
                 listing_date: str,
                 settle_month: str,
                 memo: str):
        self.stype = stype
        self.code = code
        self.name = name
        self.market = market
        self.sector = sector
        self.industry = industry
        self.listing_date = listing_date
        self.settle_month = settle_month
        self.memo = memo

    def __str__(self) -> str:
        return f"{self.stype}, {self.code}, {self.name}, {self.market}, {self.sector}, {self.industry}, {self.listing_date}, {self.settle_month}, {self.memo}"

def dict_2_stock(dict_stock):
    """
    'Code': '095570', 'Name': 'AJ네트웍스', 'Market': 'KOSPI', 'Sector': '산업용 기계 및 장비 임대업', 'Industry': '렌탈(파렛트, OA장비, 건설장비)', 'ListingDate': Timestamp('2015-08-21 00:00:00'), 'SettleMonth': '12월', 'Representative': '손삼달', 'HomePage': 'http://www.ajnet.co.kr', 'Region': '서울특별시'
    """
    return Stock(
        dict_stock["Market"],
        dict_stock["Code"],
        dict_stock["Name"],
        dict_stock["Market"],
        dict_stock["Sector"],
        dict_stock["Industry"],
        dict_stock["ListingDate"],
        dict_stock["SettleMonth"],
        f'Representative={dict_stock["Representative"]}, HomePage={dict_stock["HomePage"]}, Region={dict_stock["Region"]}'
    )

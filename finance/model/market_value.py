"""
+--------+-------------+------+-----+---------+----------------+
| id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| code   | varchar(10) | YES  |     | NULL    |                |
| open   | int(11)     | YES  |     | NULL    |                |
| high   | int(11)     | YES  |     | NULL    |                |
| low    | int(11)     | YES  |     | NULL    |                |
| close  | int(11)     | YES  |     | NULL    |                |
| volume | int(11)     | YES  |     | NULL    |                |
| change | int(11)     | YES  |     | NULL   
"""
from datetime import datetime
class_name="Stock"


class MarketValue:
    id: int
    code: str
    open_v: float
    high: float
    low: float
    close: float
    volume: int
    change: float
    updated: datetime

    def __init__(self,
                 id: int = 0,
                 code: str = "",
                 open_v: float = 0,
                 high: float = 0,
                 low: float = 0,
                 close: float = 0,
                 volume: int = 0,
                 change: float = 0,
                 updated: datetime = datetime.now()):
        self.id = 0
        self.code = code
        self.open_v = open_v
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.change = change
        self.updated = updated

    def where_by_code_and_openv_and_updated(self):
        return f'code=\"{self.code}\" and open=\"{self.open_v}\" and updated=\"{self.updated}\"'

    def __str__(self) -> str:
        return f'\"{self.id}\", \"{self.code}\", \"{self.open_v}\", \"{self.high}\", \"{self.low}\", \"{self.close}\", \"{self.volume}\", \"{self.change}\", \"{self.updated}\"'

    def __eq__(self, other):
        if self.code == other.code and self.updated.date() == other.updated.date():
            return True
        else:
            return False

    @classmethod
    def from_dict(cls, value, code, updated):
        if "Change" in value: 
            change = value["Change"]
        else:
            change = 0
        
        return MarketValue(
            code = code,
            open_v = value["Open"],
            high = value["High"],
            low = value["Low"],
            close = value["Close"],
            volume = value["Volume"],
            change = change,
            updated = updated
        )

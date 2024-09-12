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
    open_v: int
    high: int
    low: int
    close: int
    volume: int
    change: int
    updated: datetime

    def __init__(self,
                 id: int = 0,
                 code: str = "",
                 open_v: int = 0,
                 high: int = 0,
                 low: int = 0,
                 close: int = 0,
                 volume: int = 0,
                 change: int = 0,
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
            False

    @classmethod
    def from_dict(cls, value, code, updated):
        return MarketValue(
            code = code,
            open_v = value["Open"],
            high = value["High"],
            low = value["Low"],
            close = value["Close"],
            volume = value["Volume"],
            change = value["Change"],
            updated = updated
        )

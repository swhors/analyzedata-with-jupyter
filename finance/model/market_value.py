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

    def __init__(self,
                 code: str,
                 open_v: int,
                 high: int,
                 low: int,
                 close: int,
                 volume: int,
                 change: int):
        self.id = 0
        self.code = code
        self.open_v = open_v
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.change = change

    def __str__(self) -> str:
        return f'\"{self.id}\", \"{self.code}\", \"{self.open_v}\", \"{self.high}\", \"{self.low}\", \"{self.close}\", \"{self.volume}\", \"{self.change}\"'

    @classmethod
    def from_dict(cls, value):
        return Stock(
            value["Code"],
            value["Open"],
            value["High"],
            value["Low"],
            value["Close"],
            value["Volume"],
            value["Change"])
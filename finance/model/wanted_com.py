class_name="Stock"

class WantedCom:
    id: int
    code: str
    name: str
    market: str

    def __init__(self,
                 code: str,
                 name: str,
                 market: str):
        self.id = 0
        self.code = code
        self.name = name
        self.market = market

    def __str__(self) -> str:
        return f'\"{self.code}\", \"{self.name}\", \"{self.market}\"'

    @classmethod
    def from_dict(cls, wanted):
        return Stock(
            wanted["Market"],
            wanted["Code"],
            wanted["Name"])

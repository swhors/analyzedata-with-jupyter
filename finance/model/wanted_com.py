class_name="Stock"

class WantedCom:
    id: int
    code: str
    name: str
    market: str

    def __init__(self,
                 id: int = 0,
                 code: str = "",
                 name: str = "",
                 market: str = ""):
        self.id = id
        self.code = code
        self.name = name
        self.market = market

    def __str__(self) -> str:
        return f'\"{self.id}\", \"{self.code}\", \"{self.name}\", \"{self.market}\"'

    @classmethod
    def from_dict(cls, wanted):
        return Stock(
            wanted["Market"],
            wanted["Code"],
            wanted["Name"])
    
    def __eq__(self, other):
        if self.code == other.code:
            return True
        else:
            False

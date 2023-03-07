import uuid


class Insured:
    def __init__(self, name: str, b_year: int, position: str, company: str):
        self.name = name
        self.b_year = b_year
        self.position = position
        self.capital = None
        self.company = company
        self.earnings = {}
        self.uuid = uuid.uuid5(uuid.NAMESPACE_OID, self.name)

    def enter_capital(self, new_capital: int):
        self.capital = new_capital if new_capital > 0 else 0

    def enter_earnings(self, year: int, earnings: float) -> bool:
        if not isinstance(earnings, (int, float)):
            return False
        if not isinstance(year, int):
            return False
        if year < 1900:
            return False
        self.earnings[year] = earnings
        return True


# szybki test klasy
if __name__ == "__main__":
    test = Insured("Test Insured", 2000)
    print(test.name)
    print(test.uuid)

class Bill():
    """
    Object cointaining data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate():
    """
    Contains a flatmate - person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate, precision=2):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        to_pay = weight * bill.amount
        return round(to_pay,precision)



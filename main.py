class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatemate:
    """
    Creates a flatemate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill,flatemate2):
        part = self.days_in_house / (self.days_in_house + flatemate2.days_in_house)
        to_pay = bill.amount * part
        return to_pay

class PdfReport:
    """
    Create a PDF file that contains data about
    the flatmates such as their names, their due amount
    and the period
    """

    def __init__(self,filemate):
        self.filename = filemate

    def generate(self,flatmate1,flatemate2, bill):
        pass

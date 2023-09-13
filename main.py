from fpdf import FPDF
import webbrowser

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

    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon
        pdf.image('Flatmates_bill/bill_icon.png', w=30, h=30)

        #Inset Title
        pdf.set_font(family='Arial', style='B', size=24)
        pdf.cell(w=0, h=80, txt='Flatmate Report', border=1, align='C', ln=1)

        #Insert Period values
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=0, h=40,txt=bill.period,border=1, ln=1)

        #Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=100, h=40, txt='Name:' + flatmate1.name, border=1,)
        pdf.cell(w=0, h=40, txt='Due:' + str(round(flatmate1.pays(bill, flatmate2), 2)), border=1, ln=1)

        #Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt='Name:' + flatmate2.name, border=1)
        pdf.cell(w=0, h=40, txt='Due:' + str(round(flatmate2.pays(bill, flatmate1), 2)), border=1, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)

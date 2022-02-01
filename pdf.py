import subprocess
from fpdf import FPDF
from filestack import Client

class PdfReport():
    """
    Creates a Pdf file that contains data about the flatmates,
    such as their names, their due amounts, and the period
    of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # insert icon
        pdf.image("files/house.png", w=30, h=30)

        # insert title
        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # insert period label and value
        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)

        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)

        # insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=str(flatmate2.pays(bill, flatmate1)), border=0)

        pdf.output(f"output/{self.filename}")

        subprocess.Popen(f"output/{self.filename}", shell=True)


class FileSharer():

    def __init__(self, filepath, api_key="AqTbevmCxRBa8fUxGLQbiz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self,):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=f"output/{self.filepath}")
        return new_filelink.url
#Imports
from flat import Bill, Flatmate
from pdf import PdfReport, FileSharer

#User input
amount = float(input("Hey user, enter the bill amount: "))
period = input("Now enter the bill period (Eg December 2020): ")

f1 = input("Whats the name of the first flatmate? ")
f1d = int(input(f"How many days was {f1} in the house during the bill period? "))

f2 = input("Whats the name of the second flatmate? ")
f2d = int(input(f"How many days was {f2} in the house during the bill period? "))


#Logic
the_bill = Bill(amount, period)
flatmate1 = Flatmate(name=f1, days_in_house=f1d)
flatmate2 = Flatmate(name=f2, days_in_house=f2d)

print(flatmate1.name, " pays:", flatmate1.pays(bill=the_bill, other_flatmate=flatmate2))
print(flatmate2.name," pays:", flatmate2.pays(bill=the_bill, other_flatmate=flatmate1))

pdf_report = PdfReport(filename=f"Bill from {the_bill.period}.pdf")
pdf_report.generate(flatmate1,flatmate2,the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
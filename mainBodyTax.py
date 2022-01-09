from newTaxRegime import *
from OldTaxRegime import *
from OTRSurcharge import *

menu = "Welcome To The Tax Calculator"
print(menu.center(100, "*"))


def detail():
    name = input("Enter Your Name : ")
    age = int(input("Enter you age : "))
    # income = int(input("Enter your income : "))
    regime = int(
        input("Enter the tax Regime\n1) Old Regime\n2) New Regime\nChoice : "))
    return [age, regime]


f = detail()
Age, Reg = f


def category(x):
    if x > 0 and x < 60:
        return 'a'
    elif x >= 60 and x < 80:
        return 'b'
    else:
        return 'c'


cat = category(Age)

li = []
for i in range(10):
    li.append(0)


def deductions(income):
    su = 0
    print(" Please Enter the following values ".center(50,"-"))
    incIt = int(input("Income from Interest : ".rjust(45," ")))
    li[0] = incIt
    incRent = int(input("Rental income received : ".rjust(45," ")))
    incRent1 = incRent - (incRent*0.3)
    li[1] = incRent1
    incHl = int(input("Interest paid on Home loan : ".rjust(45," ")))
    li[2] = incHl

    exem = int(input("Exemptions and Deductions from Salary : ".rjust(45," ")))
    li[3] = exem
    basDed = int(input("Basic Deductions - 80C : ".rjust(45," ")))
    li[4] = basDed
    medIns = int(input("Medical Insurance - 80D : ".rjust(45," ")))
    li[5] = medIns
    eduLoan = int(input("Interest on Educational Loan - 80E : ".rjust(45," ")))
    li[6] = eduLoan
    nps = int(input("Employee's contribution to NPS - 80CCD : ".rjust(45," ")))
    li[7] = nps
    dtc = int(input("Donations to Charity - 80G : ".rjust(45," ")))
    li[8] = dtc
    inthouseLoan = int(input("Interest on Housing Loan - 80EEA : ".rjust(45," ")))
    li[9] = inthouseLoan
    for i in range(2, 10):
        su += li[i]
    newInc = income + (li[0]+li[1]) - su
    return newInc


if Reg == 2:
    income = int(input("Enter Your Income : "))
    if income <= 5000000:
        tax = income-nTaxRegime(income)
        print("Taxes Due Are : ", round(tax))
        print("Income after Tax : ", round(nTaxRegime(income)))
    else:
        tax = income-NewRegimesurcharge(income)
        print("Taxes Due Are : ", round(tax))
        print("Income after Tax : ", round(NewRegimesurcharge(income)))
elif Reg == 1:
    income = int(input("Enter Your Income : "))
    NewInc = deductions(income)
    Reg1 = {
        "a": FMBelow60(NewInc),
        "b": MFAbove60(NewInc),
        "c": Above80(NewInc)
    }
    Reg2 = {
        "a": B60Surcharge(NewInc),
        "b": surcharge6080(NewInc),
        "c": Above80Surchargee(NewInc)}
    if NewInc <= 5000000:
        tax = income - Reg1[cat]
        print("Taxes Due are : ", tax)
        print("Income after Tax is : ", round(Reg1[cat]))
    else:
        tax = income - Reg2[cat]
        print("Taxes Due are : ", tax)
        print("Income after Tax is : ", round(Reg2[cat]))
else:
    pass

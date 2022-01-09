from tkinter import *
from tkinter.font import BOLD, ITALIC
from OTRSurcharge import *
from newTaxRegime import *
from OldTaxRegime import *

root = Tk()
root.title("TAx Calculator")
root.geometry("1600x1600")
var = IntVar()
var.set(1)


f0 = Frame(root)
f0.pack(side=TOP, fill=X, pady=50)
f1 = Frame(root)
f1.pack(side=TOP, fill=X)
f2 = Frame(root)
f2.pack(side=TOP, fill=X)
f3 = Frame(root)
f3.pack(side=TOP, fill=X)
f4 = Frame(root)
f4.pack(side=TOP, fill=X)
f5 = Frame(root)
f5.pack(side=TOP, fill=X)
f6 = Frame(root)
f6.pack(side=TOP, fill=X)

# FRAME 1


label1 = Label(f0, text=" Tax Calculator ",
               font=("jokerman", 18, "bold"), fg="Red")
label1.pack()
var1 = IntVar()
var1.set(11)
lab = Label(f1, text="Regime ", font=("roboto", 16, "bold")).grid(
    row=0, column=0, pady=10, sticky=W)
Radiobutton(f1, text="Old Regime", variable=var1, value=11,
            font=("milkshake", 12, "bold")).grid(row=1, column=0)
Radiobutton(f1, text="New Regime", variable=var1,
            value=12, font=("milkshake", 12, "bold"), width=20).grid(row=1, column=1)


# FRAME 3


Label(f3, text="Basics ", font=("roboto", 16, "bold")).grid(
    row=0, column=0, pady=10, sticky=W)
Label(f3, text="Income : ", font=("milkshake", 12, "bold")).grid(
    row=1, column=0, pady=10)
e0 = Entry(f3, width=50, borderwidth=5)
Label(f3, text="Income from Interest : ", font=(
    "milkshake", 12, "bold")).grid(row=3, column=2, pady=10, sticky=E)
e1 = Entry(f3, width=50, borderwidth=5)
Label(f3, text="Rental Income Received : ", font=(
    "milkshake", 12, "bold")).grid(row=2, column=0, pady=10, sticky=E)
e2 = Entry(f3, width=50, borderwidth=5)
Label(f3, text="Interest Paid on home loan : ", font=(
    "milkshake", 12, "bold")).grid(row=2, column=2, pady=10)
e3 = Entry(f3, width=50, borderwidth=5)
Label(f3, text="Exemptions and Deductions from Salary  : ",
      font=("milkshake", 12, "bold")).grid(row=3, column=0, pady=10)
e4 = Entry(f3, width=50, borderwidth=5)
Label(f3, text="Other Income  : ",
      font=("milkshake", 12, "bold")).grid(row=4, column=0, pady=10, sticky=E)
e11 = Entry(f3, width=50, borderwidth=5)
li1 = [e0, e1, e2, e3, e4, e11]
for i in range(6):
    li1[i].insert(0, "0")
e0.grid(row=1, column=1)
e1.grid(row=3, column=3)
e2.grid(row=2, column=1)
e3.grid(row=2, column=3)
e4.grid(row=3, column=1)
e11.grid(row=4, column=1)
# Frame 4
Label(f4, text="Deductions", font=("roboto", 16, BOLD), pady=15).grid(sticky=W)

Label(f4, text="Basic Deductions - 80C : ", font=("milkshake", 12, "bold")).grid(
    row=5, column=0, pady=10, sticky=E)
e5 = Entry(f4, width=50, borderwidth=5)
Label(f4, text="Medical Insurance - 80D : ", font=(
    "milkshake", 12, "bold")).grid(row=5, column=2, pady=10, sticky=E)
e6 = Entry(f4, width=50, borderwidth=5)
Label(f4, text="Interest on Educational Loan - 80E : ", font=(
    "milkshake", 12, "bold")).grid(row=6, column=0, pady=10)
e7 = Entry(f4, width=50, borderwidth=5)
Label(f4, text="Employee's contribution to NPS - 80CCD : ", font=(
    "milkshake", 12, "bold")).grid(row=6, column=2, pady=10)
e8 = Entry(f4, width=50, borderwidth=5)
Label(f4, text="Donations to Charity - 80G : ",
      font=("milkshake", 12, "bold")).grid(row=7, column=0, pady=10, sticky=E)
e9 = Entry(f4, width=50, borderwidth=5)
Label(f4, text="Interest on Housing Loan - 80EEA : ",
      font=("milkshake", 12, "bold")).grid(row=7, column=2, pady=10, sticky=E)
e10 = Entry(f4, width=50, borderwidth=5)
Label(f4, text="Other Deductions : ",
      font=("milkshake", 12, "bold")).grid(row=8, column=0, pady=10, sticky=E)
e12 = Entry(f4, width=50, borderwidth=5)
li2 = [e5, e6, e7, e8, e9, e10, e12]
for i in range(7):
    li2[i].insert(0, "0")
e5.grid(row=5, column=1)
e6.grid(row=5, column=3)
e7.grid(row=6, column=1)
e8.grid(row=6, column=3)
e9.grid(row=7, column=1)
e10.grid(row=7, column=3)
e12.grid(row=8, column=1)
# frame 2

Label(f2, text="Age category", font=("roboto", 16, BOLD), pady=15).grid()

Radiobutton(f2, text="Below 60", variable=var, value=1,
            font=("milkshake", 12, "bold")).grid(row=4, column=0)
Radiobutton(f2, text="Between 60 & 80", variable=var,
            value=2, font=("milkshake", 12, "bold"), width=20).grid(row=4, column=1)
Radiobutton(f2, text="Above 60", variable=var, value=3,
            font=("milkshake", 12, "bold")).grid(row=4, column=2)
labelTax = Label(f4, text="Tax : ",
                 font=("milkshake", 12, "bold")).grid(row=10, column=0, pady=10, sticky=E)
ent1 = Entry(f4, width=50, borderwidth=5)
labelSal = Label(f4, text="Salary after Tax : ",
                 font=("milkshake", 12, "bold")).grid(row=10, column=2, pady=10, sticky=E)
ent2 = Entry(f4, width=50, borderwidth=5)
ent1.grid(row=10, column=1)
ent2.grid(row=10, column=3)


def exec():
    ent1.delete(0, END)
    ent2.delete(0, END)
    li = [float(e3.get()), float(e4.get()),  float(e7.get()), float(e9.get()), float(e11.get()), float(e12.get())]
    b = float(e5.get())
    if b>150000:
        b=150000
    c = float(e6.get())
    if c>100000:
        c = 100000
    d = float(e10.get()) 
    if d>150000:
        d=150000 
    a = float(e8.get())
    if a>150000:
        a=150000
    
    sal = float(e0.get())

    if var1.get() == 12:

        if sal < 5000000:
            tax = float(e0.get())-nTaxRegime(sal)
            ent1.insert(0, tax)
            ent2.insert(0, round(nTaxRegime(sal)))
        else:
            tax = float(e0.get())-NewRegimesurcharge(sal)
            ent1.insert(0, tax)
            ent2.insert(0, round(NewRegimesurcharge(sal)))
    else:
        su = 0
        for i in range(6):
            su += li[i]
        su = su+a+b+c+d
        newSal = float(e0.get()) + float(e11.get()) + \
            (float(e1.get())+(float(e2.get())-(float(e2.get())*0.3))) - su
        if newSal > 5000000 and var.get() == 1:
            tax = newSal - B60Surcharge(newSal)
            ent1.insert(0, round(tax))
            ent2.insert(0, round(sal-tax))
        elif newSal > 5000000 and var.get() == 2:
            tax = newSal - surcharge6080(newSal)
            ent1.insert(0, round(tax))
            ent2.insert(0, round(surcharge6080(sal-tax)))
        elif newSal > 5000000 and var.get() == 3:
            tax = newSal - Above80Surchargee(newSal)
            ent1.insert(0, round(tax))
            ent2.insert(0, round(Above80Surchargee(sal-tax)))
        elif newSal < 5000000 and var.get() == 1:
            tax = newSal - FMBelow60(newSal)
            ent1.insert(0, round(tax))
            ent2.insert(0, round(sal-tax))
        elif newSal < 5000000 and var.get() == 2:
            tax = newSal - MFAbove60(newSal)
            ent1.insert(0, round(tax))
            ent2.insert(0, round(MFAbove60(sal-tax)))
        else:
            tax = newSal - Above80(newSal)
            ent1.insert(0, round(tax))
            ent2.insert(0, round(Above80(sal-tax)))


Button(f5, text="Calculate", font=("roboto", 12, BOLD),
       border=5, command=exec).pack(anchor=CENTER, pady=20)


root.mainloop()

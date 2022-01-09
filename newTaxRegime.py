# new TAx regime is common for all
def nTaxRegime(inc):

    bracket = [250000, 500000, 750000, 1000000, 1250000, 1500000, 5000000]
    rate = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
    tax = [0, 12500, 37500, 75000, 125000, 187500]

    if inc < 250000:
        return inc
    else:
        for i in range(0, 7):
            if inc < bracket[i]:
                newS = inc-bracket[i-1]
                tax1 = (newS*rate[i]) + tax[i-1]
                Sal = inc - tax1 - (tax1*0.04)
                return Sal


def NewRegimesurcharge(inc):
    if inc > 5000000 and inc <= 10000000:
        newS = inc-1500000
        tax1 = (newS*0.33) + 206250
        Sal = inc - tax1 - (tax1*0.04)
        return Sal
    elif inc > 10000000:
        newS = inc-1500000
        tax1 = (newS*0.345) + 215625
        Sal = inc - tax1 - (tax1*0.04)
        return Sal

#new TAx regime is common for all
i = int(input("Sal"))
def FMBelow60(inc):
    
    bracket = [250000, 500000, 1000000, 5000000]
    rate = [0, 0.05, 0.2, 0.3]
    tax = [0, 12500, 112500]

    if inc< 250000:
        return inc
    else :
        for i in range(0,4):
            if inc<bracket[i]:
                newS = inc-bracket[i-1]
                tax1 = (newS*rate[i]) + tax[i-1]
                Sal = inc - tax1 - (tax1*0.04)
                return Sal
print(FMBelow60(i))
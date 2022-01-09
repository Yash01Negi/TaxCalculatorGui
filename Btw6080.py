def MFAbove60(inc):
    
    bracket = [300000, 500000, 1000000, 5000000]
    rate = [0, 0.05, 0.2, 0.3]
    tax = [0, 10000, 110000]

    if inc< 300000:
        return inc
    else :
        for i in range(0,4):
            if inc<bracket[i]:
                newS = inc-bracket[i-1]
                tax1 = (newS*rate[i]) + tax[i-1]
                Sal = inc - tax1 - (tax1*0.04)
                return Sal


def Above80Surchargee(inc):
    
    if inc>5000000 and inc<=10000000:
            newS = inc-1000000
            tax1 = (newS*0.33) + 110000
            Sal = inc - tax1 - (tax1*0.04)
            print(tax1)
            return Sal
    elif inc>10000000:
            newS = inc-1000000
            tax1 = (newS*0.345) + 115000
            Sal = inc - tax1 - (tax1*0.04)
            print(tax1)
            return Sal

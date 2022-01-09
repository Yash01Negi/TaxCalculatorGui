def NewRegimesurcharge(inc):
        if inc>5000000 and inc<=10000000:
            newS = inc-1500000
            tax1 = (newS*0.33) + 206250 
            Sal = inc - tax1 - (tax1*0.04)
            print(tax1)
            return Sal
        elif inc>10000000:
            newS = inc-1500000
            tax1 = (newS*0.345) + 215625
            Sal = inc - tax1 - (tax1*0.04)
            print(tax1)
            return Sal

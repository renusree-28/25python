salary=int(input("enter your salary:"))
if salary<=250000:
    print("tax is 0")
elif salary<=500000:
    tax=salary-250000
    print("calculated tax is",(tax*5)/100)
elif salary<=1000000:
    tax=salary-500000
    print("calculated tax is",(250000*5)/100+(tax*7)/100)
else:
    tax=salary-1000000
    print("calculated tax is",(250000*5)/100+(500000*7)/100+(tax*10)/100)
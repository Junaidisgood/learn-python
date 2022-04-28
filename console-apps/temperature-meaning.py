temp = int(input("Enter temperature: "))
if temp < 32:
    print("Frozen ice")
    pass
elif temp > 32 & temp < 212 :
    print("Liquid water")
    pass
elif temp > 212:
    print("Gaseous steam")
    pass
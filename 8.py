def divisibleornot(a):
    if(a%8==0):
        return "divisible"
    else:
        return "not divisible"

x=int(input("enter a number"))
result = divisibleornot(x)
print(result)
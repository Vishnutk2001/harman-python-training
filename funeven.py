def checkevenorodd(a):
    if(a%2==0):
        return "even"
    else:
        return "odd"

x=int(input("enter a number"))
result = checkevenorodd(x)
print(result)
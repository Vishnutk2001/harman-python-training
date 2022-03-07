def smallnumber(a,b,c):
    if(a<b):
        return "a is smaller"
    elif(b<c):
        return "b is smaller"
    else:
        return "c is smaller"

x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
result = smallnumber(x,y,z)
print(result)
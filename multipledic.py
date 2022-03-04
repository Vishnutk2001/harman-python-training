booklist= []
count = int(input("enter the count"))
for i in range(0,count):
    bname = input("enter name")
    price = input("enter price")
    aname = input("enter name")
    publish = input("enter year")
bookdic = [ {"bname":"a",
         "price":"2",
         "aname":"b",
         "publish":"c"} ]
booklist.append(bookdic)
print(booklist)
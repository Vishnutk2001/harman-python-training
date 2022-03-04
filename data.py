studentdata = [
    {"name": "abc",
     "marks": [
         {"eng": 35,"science": 40}
     ]
     },
    {"name":"bcd",
     "marks": [
         {"eng": 45,"science": 50}
         ]
     }]
for i in studentdata:
    print(i["name"])
    for j in i["marks"]:
        print(j["eng"])
        print(j["science"])
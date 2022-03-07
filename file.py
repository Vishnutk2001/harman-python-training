import json as j

data = {"name":"ram","status":"student"}
jsondata=j.dumps(data)


myjsonData = j.loads(jsondata) #parsing

print(myjsonData["name"])
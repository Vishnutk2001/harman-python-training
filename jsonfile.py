import json as j

data = '{"name":"ram","status":"student"}'


myjsonData = j.loads(data) #parsing

print(myjsonData["name"])
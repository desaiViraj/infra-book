import json

servers = [
    {
        "hostname": "web01",
        "cpu": 35
    },
    {
        "hostname": "db01",
        "cpu": 92
    },
    {
        "hostname": "cache01",
        "cpu": 55
    }
]

with open("server.json", "w") as file:
   json.dump(servers,file,indent=4)

with open("server.json") as file:
    loaded = json.load(file)
    print(type(loaded))

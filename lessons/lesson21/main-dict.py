import json

server = {
    "hostname": "web01",
    "cpu": 35,
    "memory": 60,
    "disk": 55
}

with open("report.json", "w") as file:
    json.dump(server, file, indent=4)

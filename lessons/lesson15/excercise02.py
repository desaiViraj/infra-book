servers = [
    {
        "hostname": "web01",
        "cpu": 35,
        "memory": 60,
        "disk": 55
    },
    {
        "hostname": "db01",
        "cpu": 92,
        "memory": 81,
        "disk": 90
    },
    {
        "hostname": "cache01",
        "cpu": 55,
        "memory": 42,
        "disk": 30
    }
]

for server in servers:
   print("==========================")
   print("Hostname    :", server["hostname"])
   print("CPU         :", server["cpu"])
   print("Memory      :", server["memory"])
   print("Disk        :", server["disk"])

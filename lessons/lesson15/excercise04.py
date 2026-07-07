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

def print_server(server):
   print("==========================")
   print("Hostname    :", server["hostname"])
   print("CPU         :", server["cpu"], get_status(server["cpu"]))
   print("Memory      :", server["memory"], get_status(server["memory"]))
   print("Disk        :", server["disk"], get_status(server["disk"]))

def get_status(value):
    if value >= 90:
       return "CRITICAL"
    elif value >= 80:
       return "WARNING"
    else:
       return "HEALTHY"

for server in servers:
    print_server(server)

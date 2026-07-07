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
   print("Overall     :", overall_status(server))

def get_status(value):
    if value >= 90:
       return "CRITICAL"
    elif value >= 80:
       return "WARNING"
    else:
       return "HEALTHY"

def overall_status(status):
    if get_status(server["cpu"]) == "CRITICAL" or get_status(server["memory"]) == "CRITICAL" or get_status(server["disk"]) == "CRITICAL":
       return "CRITICAL"
    elif get_status(server["cpu"]) == "WARNING" or get_status(server["memory"]) == "WARNING" or get_status(server["disk"]) == "WARNING":
       return "WARNING"
    else:
       return "HEALTHY"
    
for server in servers:
    print_server(server)

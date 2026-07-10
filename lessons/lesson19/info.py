import health

server = {
    "hostname": "web01",
    "cpu": 92,
    "memory": 81,
    "disk": 45
}

#cpu = int(input("Enter CPU: "))

#print(health.get_status(35))
#print(health.get_status(82))
#print(health.get_status(95))

#print(health.get_status(server["cpu"]))

print("CPU    :", health.get_status(server["cpu"]))
print("Memory :", health.get_status(server["memory"]))
print("Disk   :", health.get_status(server["disk"]))

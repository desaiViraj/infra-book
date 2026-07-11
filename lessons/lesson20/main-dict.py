import json

def print_info(server):
   print("===============================")
   print("         SYSTEM INFO           ")
   print("===============================")
   print("Hostname: ", server["hostname"])
   print("CPU: ", server["cpu"])
   print("Memory: ", server["memory"])
   print("Disk: ", server["disk"])
   print()

with open("server.json") as file:
    server = json.load(file)

print_info(server)

print(server)
print(type(server))
print(server["hostname"])


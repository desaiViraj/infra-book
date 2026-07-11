import json

def print_info(values):
    print("=============================")
    print("         SERVER INFO         ")
    print("=============================")
    print("Hostname: ", values["server"]["hostname"])
    print("IP Address: ", values["server"]["ip"])
    print("CPU: ", values["resources"]["cpu"])
    print("Memory: ", values["resources"]["memory"])
    print("Disk: ", values["resources"]["disk"])
    print()

with open("server.json") as file:
    values = json.load(file)

print_info(values)

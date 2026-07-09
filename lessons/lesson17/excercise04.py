with open("cpu.log") as file:
    logs = file.readlines()

def get_status(value):
    if value >= 90:
       return "CRITICAL"
    elif value >= 80:
       return "WARNING"
    else:
       return "HEALTHY"

for log in logs:
    parts = (log.strip())
    lists = parts.split(",")
    #print(parts)
    cpu = int(lists[1])
    #print(cpu)
    #print(parts[1])
    print("Server: ", lists[0], "CPU: ", lists[1], get_status(cpu))

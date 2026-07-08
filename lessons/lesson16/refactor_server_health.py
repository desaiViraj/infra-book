hostname = input("Enter Hostname: ")
cpu = int(input("Enter CPU: "))
memory = int(input("Enter Memory: "))
disk = int(input("Enter Disk: "))
server = {
    "hostname": hostname,
    "cpu": cpu,
    "memory": memory,
    "disk": disk
}

def get_status(value):
   if value >= 90:
      return "CRITICAL"
   elif value >= 80:
      return "WARNING"
   else:
      return "HEALTHY"

def print_report(server):
   print()
   metrics = ["cpu", "memory", "disk"]
   for metric in metrics:
       print(metric,"     : ", server[metric], get_status(server[metric]))
   
print_report(server)

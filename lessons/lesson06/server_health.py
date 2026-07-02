# Lesson 06
# Program: Server Health Checker
# Author: Viraj

hostname = input("Enter Hostname: ")
cpu_usage = int(input("Enter CPU usage: "))
memory_usage = int(input("Enter Memory usage: "))
disk_usage = int(input("Enter Disk usage: "))
print("===================================")
print("       SYSTEM RESOURCE INFO        ")
print("===================================")
print()
if cpu_usage >= 90 or memory_usage >= 90 or disk_usage >= 90:
    print("Server", hostname, "is Critical")
else:
    print("Server", hostname, "is Healthy")

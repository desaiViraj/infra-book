# Lesson 05-1
# Program: CPU Health Checker
# Author: Viraj

hostname = input("Enter Hostname: ")
cpu_usage = int(input("Enter CPU Usage: "))
memory_usage = int(input("Enter Memory Usage: "))
disk_usage = int(input("Enter Disk Usage: "))
print("========================")
print("  SYSTEM HEALTH REPORT  ")
print("========================")
print()
print("Hostname     :", hostname)
print()
if cpu_usage >= 90:
   print(" CPU      : Critical")
elif cpu_usage >= 80:
   print(" CPU      : Warning")
else:
   print(" CPU      : Healthy")

if memory_usage >= 90:
   print(" Memory   : Critical")
elif memory_usage >= 80:
   print(" Memory   : Warning")
else:
   print(" Memory   : Healthy")

if disk_usage >= 90:
   print(" Disk     : Critical")
elif disk_usage >= 80:
   print(" Disk     : Warning")
else:
   print(" Disk     : Healthy")

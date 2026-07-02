# Lesson 05
# Program: CPU Health Checker
# Author: Viraj
cpu_usage = int(input("Enter the CPU Usage: "))
memory_usage = int(input("Enter Memory Usage: "))

if memory_usage >= 90:
   print(" Memory Usage: Critical")
elif memory_usage >= 80:
   pritn("Memory Usage: Warning")
else:
   print("Memory Usage: Healthy")

if cpu_usage >= 90:
   print("CPU Usage: Critical")
elif cpu_usage >= 80:
   print("CPU Usage: Warning")
else:
   print("CPU Usage: Healthy")

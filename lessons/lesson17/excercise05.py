with open("app.log") as file:
    logs = file.readlines()

info = 0
warning = 0
error = 0
total = 0

for line in logs:
   total += 1 
   if "ERROR" in line:
       error += 1
   elif "WARNING" in line:
       warning += 1
   elif "INFO" in line:
       info += 1

def overall_status():
    if error >= 2:
       return("Overall Status : CRITICAL")
    elif warning >= 2:
       return("Overall Status : WARNING")
    else:
       return("Overall Status : HEALTHY")

print("============================")
print("      LOG ANALYSIS          ")
print("============================")
print("Total Lines :", total)
print("INFO Count:", info)
print("WARNING Count:", warning)
print("ERROR Count:", error)
print(overall_status())

import json
import report
 
with open("server.json") as file:
    server_data = json.load(file)

for server in server_data:
    print("==========================")
    report.print_report(server)

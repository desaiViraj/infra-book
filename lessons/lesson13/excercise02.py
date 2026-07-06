servers = [
    "web01",
    "web02",
    "db01"
]

def check(server):
    print("Checking", server)

for server in servers:
    check(server)

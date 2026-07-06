servers = [
    "prod-web01",
    "dev-web01",
    "prod-db01",
    "qa-api01"
]

for server in servers:
   if (server.startswith("prod-")):
       print(server)

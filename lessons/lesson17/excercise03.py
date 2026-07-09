file = open("inventory.txt")
content = file.readlines()
for server in content:
    print("Server: ", server.strip())

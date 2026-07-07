pod = {
    "name": "mongodb-rs-0-2",
    "namespace": "database",
    "status": "Running",
    "restarts": 0
}

print("Pod Name    :", pod["name"])
print("Namespace   :", pod["namespace"])
print("Status      :", pod["status"])
print("Restarts    :", pod["restarts"])

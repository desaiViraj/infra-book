pods = [
    "mongodb-rs-0-0",
    "mongodb-rs-0-1",
    "mongodb-rs-0-2"
]

for pod in pods:
    position = pod.split("-")
    print("Pod Number: ", pod[-1])

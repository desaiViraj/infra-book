import health

health.threshold = 75
def print_report(server):
    print("CPU", health.get_status(server["cpu"]))
    print("Memory", health.get_status(server["memory"]))
    print("Disk", health.get_status(server["disk"]))

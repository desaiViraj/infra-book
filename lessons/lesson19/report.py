import health

def print_report(server):
    print("CPU", health.get_status(server["cpu"]))
    print("Memory", health.get_status(server["memory"]))
    print("Disk", health.get_status(server["disk"]))

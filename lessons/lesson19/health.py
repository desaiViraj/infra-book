def get_status(value):
    if value >= 90:
       return "CRITICAL"
    elif value >= 80:
       return "WARNING"
    else:
       return "HEALTHY"

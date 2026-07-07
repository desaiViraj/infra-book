def free_disk(total,used):
    return (total - used)


remaining = free_disk(500,420)

print("Free Disk", remaining)

disk_size = int(input("Enter Total Disk Size: "))
disk_used = int(input("Enter Used Disk Size: "))
free_disk = disk_size - disk_used
usage_percentage = ( disk_used / disk_size ) * 100
if usage_percentage > 80:
	print("WARNING: Disk usage is high!")
print("========================")
print("   DISK USAGE REPORT    ")
print("========================")
print
print("Total Disk :", disk_size)
print("Used Disk  :", disk_used)
print("Free Disk  :", free_disk)
print("Usage	  :", usage_percentage)

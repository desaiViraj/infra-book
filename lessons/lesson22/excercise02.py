import subprocess

result = subprocess.run(["hostname"], capture_output=True, text=True)
#print(type(result))
hostname = result.stdout
#print(type(hostname))
print("========================")
print("   SYSTEM INFORMATION   ")
print("========================")
print("Hostname: ",hostname.strip())

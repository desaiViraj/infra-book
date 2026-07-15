import subprocess

result = subprocess.run(
    ["df", "-h"],
    capture_output=True,
    text=True
)
print(type(result))

lines = result.stdout.splitlines()
print(type(lines))

for line in lines:
    print(line.split())
    parts = line.split()
    print(parts[4])
    usage = parts[4]
    print(usage.split("%")) 

import subprocess

result = subprocess.run(["hostname"], capture_output = True, text = True)

print(result)
print(result.stdout)
print(type(result.stdout))

import subprocess

try:
    subprocess.run(["abcd123"])
except FileNotFoundError:
    print("Command does not exist.")

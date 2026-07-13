import subprocess

try:
    result_hostname = subprocess.run(["hostname"], capture_output=True, text=True)
    result_user = subprocess.run(["whoami"], capture_output=True, text=True)

    hostname = result_hostname.stdout.strip()
    current_user = result_user.stdout.strip()

    print("==============================")
    print("      SYSTEM INFORMATION      ")
    print("==============================")

    print("Hostname: ", hostname)
    print("User    : ", current_user)

except FileNotFoundError:
    print("Command not found")

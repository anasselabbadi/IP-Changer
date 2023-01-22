import subprocess

# Get the current IP address
try:
    current_ip = subprocess.run("netsh interface ip show address \"Wi-Fi\"", shell=True, capture_output=True).stdout.decode().split("\r\n")[-2]
except Exception as e:
    print(f'Error occured while getting the current IP address: {e}')
    exit()

# Prompt the user for their desired IP address
new_ip = input("Enter your desired IP address: ")

# Create the command to change the IP address
command = "netsh interface ip set address \"Wi-Fi\" static {} 255.255.255.0".format(new_ip)

# Execute the command
try:
    subprocess.run(command, shell=True)
except Exception as e:
    print(f'Error occured while changing the IP address: {e}')
    exit()

# Confirm the IP address change
try:
    new_ip = subprocess.run("netsh interface ip show address \"Wi-Fi\"", shell=True, capture_output=True).stdout.decode().split("\r\n")[-2]
    print("IP address successfully changed from {} to {}".format(current_ip,new_ip))
except Exception as e:
    print(f'Error occured while getting the new IP address: {e}')

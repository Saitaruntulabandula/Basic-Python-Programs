import subprocess
response = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("Using dir command to list files and directory")
print(response)
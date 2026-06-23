import subprocess

password = "admin123"

cmd = input("Enter command: ")
subprocess.call(cmd, shell=True)
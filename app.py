import subprocess
import os

cmd = input("Enter command: ").split()
subprocess.run(cmd)

password = os.getenv("APP_PASSWORD")
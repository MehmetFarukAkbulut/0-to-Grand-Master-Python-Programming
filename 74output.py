import subprocess

with open("74cikti.txt", "w") as dosya:
    dosya.write(subprocess.check_output("74win-eurasia.py", shell=True).decode())
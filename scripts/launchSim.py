import os
import sys
import subprocess

def run_commands(n):
    command = ""
    for i in range(n):
        command += f'./../../build/zephy/zephyr.exe -no-rt -s=hello_world -d=${i} &'

    command = command[:-1]    

    simCommand = f'cd ../../../tools/bsim/bin && ./bs_ksim_phy_v1 -D=2 -s=hello_world -channel=multiatt -crcerr_data -defmodem=ksim_simple -nodump -sim_length=60e6 -v=9 &'

    subprocess.run(f"gnome-terminal -- bash -c '{simCommand}; exec bash'", shell=True)
    subprocess.run(f"gnome-terminal -- bash -c '{command}; exec bash'", shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_commands.py <number_of_times>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer")
        sys.exit(1)

    run_commands(n)

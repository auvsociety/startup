#!/usr/bin/python3

import os
import subprocess
import datetime

def create_log_directory(folder_path, current_time):
    
    log_directory = f"{folder_path}/logs/{os.path.join(current_time)}"
    os.makedirs(log_directory, exist_ok=True)
    return log_directory

def run_scripts_in_folder(folder_path, current_time):
    current_script = os.path.basename(__file__)
    scripts = [file for file in os.listdir(folder_path) if file != current_script and os.path.isfile(file) and file.endswith('.start')]

    if not scripts:
        print("No scripts found. Exiting.")
        return

    print(f"Found {len(scripts)} startup files:\n")
    [print(script) for script in scripts]

    processes = []
    
    log_directory = create_log_directory(folder_path, current_time)

    for script in scripts:
        log_file = os.path.join(log_directory, f"{script}.log")
        f = open(log_file, 'w', buffering=1)
        processes.append(subprocess.Popen([os.path.join(folder_path, script)], stdout=f, stderr=f))
    
    for process in processes:
        process.communicate()
    
    print("All processes finished.")

if __name__ == "__main__":
    folder_path = "/home/jetson/startup"
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    print(f"Starting script at {current_time}")

    run_scripts_in_folder(folder_path, current_time)


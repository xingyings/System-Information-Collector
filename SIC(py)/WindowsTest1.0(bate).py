import subprocess
import os

def get_cpu_info():
    command = "wmic cpu get name, currentclockspeed"
    result = subprocess.check_output(command, shell=True, text=True)
    return result.strip()

def get_memory_info():
    command = "wmic computersystem get totalphysicalmemory"
    result = subprocess.check_output(command, shell=True, text=True)
    return result.strip()

def get_graphics_card_info():
    command = "wmic path win32_videocontroller get name, driverdate, driverversion"
    result = subprocess.check_output(command, shell=True, text=True)
    return result.strip()

def save_to_file(data, file_path):
    with open(file_path, 'w') as f:
        f.write(data)

def main():
    info = []
    info.append("CPU Information:\n")
    info.append(get_cpu_info() + "\n\n")

    info.append("Memory Information:\n")
    info.append(get_memory_info() + "\n\n")

    info.append("Graphics Card Information:\n")
    info.append(get_graphics_card_info())

    file_path = r"C:\Program Files (x86)\xingying\error.log"
    save_to_file(''.join(info), file_path)
    print(f"Information saved to {file_path}")

if __name__ == "__main__":
    main()

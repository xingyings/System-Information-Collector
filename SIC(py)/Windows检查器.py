import os
import platform
import subprocess
import datetime
import concurrent.futures

# 隐藏命令提示框
def run_hidden(command):
    try:
        if platform.system() == 'Windows':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        else:
            startupinfo = None
        
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                               startupinfo=startupinfo)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"执行命令出错: {e}"

# 收集系统信息
def collect_system_info():
    # 使用WMIC命令获取CPU信息
    cpu_info = run_hidden(['wmic', 'cpu', 'get', 'Name,CurrentClockSpeed'])
    
    # 使用WMIC命令获取内存信息
    memory_info = run_hidden(['wmic', 'computersystem', 'get', 'TotalPhysicalMemory'])
    
    # 使用WMIC命令获取显卡信息
    graphics_card_info = run_hidden(['wmic', 'path', 'Win32_VideoController', 'get', 'Name,AdapterRAM,DriverDate,DriverVersion'])
    
    # 获取操作系统版本
    os_info = platform.platform()
    
    # 获取磁盘空间信息
    disk_info = run_hidden(['wmic', 'logicaldisk', 'get', 'Caption,FreeSpace,Size'])
    
    # 获取网络适配器信息
    network_adapters = run_hidden(['ipconfig'])
    
    # 获取系统硬件信息
    system_hw_info = run_hidden(['systeminfo'])
    
    info = [
        "操作系统版本:\n" + os_info + "\n",
        "CPU 信息:\n" + cpu_info + "\n",
        "内存信息:\n" + memory_info + "\n",
        "显卡信息:\n" + graphics_card_info + "\n",
        "磁盘空间信息:\n" + disk_info + "\n",
        "网络适配器信息:\n" + network_adapters + "\n",
        "系统硬件信息:\n" + system_hw_info + "\n"
    ]
    
    return '\n'.join(info)

# 保存到文件
def save_to_file(data, file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)

# 主函数
def main():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    target_dir = r'D:\xingying'
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    file_name = f"Windows[{timestamp}].zip"
    file_path = os.path.join(target_dir, file_name)
    
    # 收集系统信息
    system_info = collect_system_info()
    
    # 保存到文件
    save_to_file(system_info, file_path)
    
    print(f"系统信息已收集并保存到: {file_path}")

if __name__ == "__main__":
    main()

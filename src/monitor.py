import psutil
import os
import time
import sys
from datetime import datetime

def get_size(bytes, suffix="B"):
    """
    Масштабирует байты в правильный формат (ГБ, МБ и т.д.)
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def clear_screen():
    """Очищает терминал"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        while True:
            clear_screen()
            print(f"🚀 --- System Vibe Monitor --- {datetime.now().strftime('%H:%M:%S')} ---")
            
            # CPU
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"\n💻 CPU Usage: {cpu_usage}%")
            
            # RAM
            vm = psutil.virtual_memory()
            print(f"🧠 RAM: {get_size(vm.used)} / {get_size(vm.total)} ({vm.percent}%)")
            
            # Disk (Внешний SSD)
            # Пытаемся найти путь к внешнему диску
            ssd_path = "/Volumes/SSD_EXTERNAL"
            if os.path.exists(ssd_path):
                disk = psutil.disk_usage(ssd_path)
                print(f"💾 SSD ({ssd_path}): {get_size(disk.used)} / {get_size(disk.total)} ({disk.percent}%)")
            else:
                print(f"⚠️  SSD ({ssd_path}) не найден.")

            # Top Processes
            print("\n🔝 Top 5 Processes (CPU):")
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Сортируем и выводим топ-5 (фильтруем None в cpu_percent)
            top_procs = sorted(
                [p for p in processes if p.get('cpu_percent') is not None], 
                key=lambda x: x['cpu_percent'], 
                reverse=True
            )[:5]
            for p in top_procs:
                print(f"  - {p['name']} (PID: {p['pid']}): {p['cpu_percent']}%")

            print("\n[ Нажмите Ctrl+C для выхода ]")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n👋 Мониторинг остановлен.")

if __name__ == "__main__":
    main()

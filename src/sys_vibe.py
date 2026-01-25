import sys
import shutil
import os
import platform

def get_free_space(path):
    usage = shutil.disk_usage(path)
    return usage.free / (1024**3)  # GB

def main():
    py_version = platform.python_version()
    interpreter = sys.executable
    
    # Путь к текущему разделу
    current_path = os.path.abspath(os.sep)
    free_gb = get_free_space(current_path)

    # Проверка venv
    is_venv = sys.prefix != sys.base_prefix
    
    # Проверка внешнего диска (для macOS /Volumes/)
    is_external = sys.prefix.startswith('/Volumes/')

    print("🌟 --- System Vibe Check --- 🌟")
    print(f"🐍 Python Version: {py_version}")
    print(f"⚙️  Interpreter: {interpreter}")
    print(f"💾 Free Space: {free_gb:.2f} GB")
    
    print("\n--- Status ---")
    if is_venv:
        print("✅ Virtual Environment: Active")
    else:
        print("❌ Virtual Environment: Not detected")
        
    if is_external:
        print("🚀 External Disk: Yes (Working from /Volumes/)")
    else:
        print("🏠 External Disk: No (Local storage)")

if __name__ == "__main__":
    main()

import argparse
from src import sys_vibe, weather_vibe, monitor

def main():
    parser = argparse.ArgumentParser(description="Prompt Design Utility")
    parser.add_argument("command", choices=["sys", "weather", "monitor"], help="Command to run")
    
    args = parser.parse_args()

    if args.command == "sys":
        sys_vibe.main()
    elif args.command == "weather":
        weather_vibe.main()
    elif args.command == "monitor":
        monitor.main()

if __name__ == "__main__":
    main()

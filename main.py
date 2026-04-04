import argparse


def main():
    parser = argparse.ArgumentParser(description="Prompt Design Utility")
    parser.add_argument("command", choices=["sys", "weather", "monitor", "blush"], help="Command to run")

    args = parser.parse_args()

    if args.command == "sys":
        from src import sys_vibe

        sys_vibe.main()
    elif args.command == "weather":
        from src import weather_vibe

        weather_vibe.main()
    elif args.command == "monitor":
        from src import monitor

        monitor.main()
    elif args.command == "blush":
        from src import blush_demo

        blush_demo.main()


if __name__ == "__main__":
    main()

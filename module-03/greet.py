import argparse


def main():
    parser = argparse.ArgumentParser(description="Greeting CLI")
    subparsers = parser.add_subparsers(dest="command")

    hello_parser = subparsers.add_parser("hello", help="Print a greeting")
    hello_parser.add_argument("name", help="Name to greet")
    hello_parser.add_argument("--upper", action="store_true", help="Print in uppercase")

    args = parser.parse_args()

    if args.command == "hello":
        message = f"Hello, {args.name}!"
        print(message.upper() if args.upper else message)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

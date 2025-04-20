import argparse
from .resolver import get_path

def main():
    parser = argparse.ArgumentParser(description="Resolve paths reliably across environments.")
    parser.add_argument("path", help="Relative path to resolve")
    parser.add_argument("--root", help="Optional custom root directory", default=None)
    args = parser.parse_args()

    try:
        resolved = get_path(args.path, root=args.root)
        print(resolved)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()

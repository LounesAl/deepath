import argparse
from .resolver import deepath

def main():
    parser = argparse.ArgumentParser(description="Resolve paths reliably across environments (dev or frozen).")
    parser.add_argument("path", help="Relative path to resolve")
    args = parser.parse_args()

    try:
        print(deepath(args.path))
    except FileNotFoundError as e:
        print(f"[deepath] {e}")

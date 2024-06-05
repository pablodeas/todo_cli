import argparse

list = argparse.ArgumentParser(
    description="List all notes.",
    epilog="List all notes available in the database."
)

list.add_argument("list", metavar="list", type=str, help="Call for the list.")

args = list.parse_args()
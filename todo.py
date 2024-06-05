"""
# Author:       Pablo Andrade
# Created:      05/06/2024
# Version:      0.0.1
# Description:  A ToDo app for fast usage
"""

import sqlite3
import argparse

def list_db(cur):
    for row in cur.execute("""SELECT Id, Date as Title, Text as Body FROM note;"""):
        print(f"> {row[0]}: {row[1]} - {row[2]}")

def insert_db(con, cur, note_title, note_body):
    cur.execute("INSERT INTO note (Date, Text) VALUES (?,?)", (note_title, note_body))
    con.commit()

def delete_db(con, cur, Id):
    cur.execute("DELETE FROM note WHERE ID = ?;", (Id,))
    con.commit()

def main():
    parser = argparse.ArgumentParser(description="Todo CLI", epilog="Manage todo notes.")
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser('list', help="List all notes.")
    list_parser.set_defaults(func=list_db)

    insert_parser = subparsers.add_parser('insert', help="Insert a new note.")
    insert_parser.add_argument("note_title", metavar="note_title", type=str, help="Title of the note.")
    insert_parser.add_argument("note_body", metavar="note_body", type=str, help="Body of the note.")
    insert_parser.set_defaults(func=insert_db)

    delete_parser = subparsers.add_parser('delete', help="Delete a note.")
    delete_parser.add_argument("Id", metavar="Id", type=int, help="Id of the note to delete")
    delete_parser.set_defaults(func=delete_db)

    args = parser.parse_args()

    con = sqlite3.connect("./todo.db")
    cur = con.cursor()

    try:
        if args.command == 'list':
            args.func(cur)
        elif args.command == 'insert':
            args.func(con, cur, args.note_title, args.note_body)
        elif args.command == 'delete':
            args.func(con, cur, args.Id)
        else:
            parser.print_help()
    except AttributeError:
        parser.print_help()
    finally:
        con.close()

if __name__ == "__main__":
    main()

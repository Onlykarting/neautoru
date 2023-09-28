import sqlite3 as db
from tkinter import *
from loop import loop

try:
    connect = db.connect("C:/projects/autoru/auto_db.db")
    cursor = connect.cursor()
    print(".\n.\n.\n.\n.\n.\nConnection successfully\n----------------------\n")
except db.Error as error:
    print("Invalid connection\n----------------------\n", error)


def main():
    loop()


if __name__ == "__main__":
    main()
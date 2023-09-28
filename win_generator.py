import random as rn
import sqlite3 as db

connect = db.connect("C:/projects/autoru/auto_db.db")
cursor = connect.cursor()


def list_to_str(arr):
    ans = ""
    for i in arr:
        ans += str(i)
    return ans


def win_create():
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    abc2 = ["A", "B", "C", "D", "E", "F", "G", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    abc3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_symb = list_to_str(rn.sample(abc, 6))
    second_symb = list_to_str(rn.sample(abc2, 5))
    third_symb = list_to_str(rn.sample(abc3, 6))
    win = first_symb + second_symb + third_symb
    return win


def win_generate(num):
    for i in range(num):
        win = win_create()
        req = "INSERT INTO wins VALUES ('" + win + "')"
        cursor.execute(req)
    connect.commit()
    return True


def win_generate_to_car():
    win = win_create()
    req = "INSERT INTO wins VALUES ('" + win + "')"
    cursor.execute(req)
    connect.commit()
    return win

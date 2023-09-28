from tkinter import *
import sqlite3 as db

connect = db.connect("C:/projects/autoru/auto_db.db")
cursor = connect.cursor()


def push_car():
    global valid_win
    add_car_window.deiconify()
    if brand.get() != "":
        for row in cursor.execute("""SELECT * FROM wins win"""):
            for i in row:
                if i == win.get():
                    valid_win = "True"

        req = "INSERT INTO cars VALUES ('" + brand.get() + "', '" + model.get() + "', '" + win.get() + "',  '" + valid_win + "', '" + mileage.get() + "', '" + reg_year.get() + "', '" + price.get() + "')"
        cursor.execute(req)
        connect.commit()


add_car_window = Tk("Add_car")
add_car_window.title("NEauto.ru (Add new car)")
add_car_window.geometry("400x300")

brand = StringVar()
model = StringVar()
win = StringVar()
valid_win = "False"
mileage = StringVar()
reg_year = StringVar()
price = StringVar()

lb_brand = Label(add_car_window, text="Brand:", width=15, height=1, font="Arial 12").grid(row=0)
lb_model = Label(add_car_window, text="Model:", width=15, height=1, font="Arial 12").grid(row=1)
lb_win = Label(add_car_window, text="WIN:", width=15, height=1, font="Arial 12").grid(row=2)
lb_mileage = Label(add_car_window, text="Mileage:", width=15, height=1, font="Arial 12").grid(row=3)
lb_reg_year = Label(add_car_window, text="Registration year:", width=15, height=1, font="Arial 12").grid(row=4)
lb_price = Label(add_car_window, text="Price:", width=15, height=1, font="Arial 12").grid(row=5)

e_brand = Entry(add_car_window, textvariable=brand).grid(row=0, column=1)
e_model = Entry(add_car_window, textvariable=model).grid(row=1, column=1)
e_win = Entry(add_car_window, textvariable=win).grid(row=2, column=1)
e_mileage = Entry(add_car_window, textvariable=mileage).grid(row=3, column=1)
e_reg_year = Entry(add_car_window, textvariable=reg_year).grid(row=4, column=1)
e_price = Entry(add_car_window, textvariable=price).grid(row=5, column=1)

btn_add = Button(add_car_window, text="Add", width=10, height=1, font="Arial 14", command=push_car).grid(row=6, column=1)

add_car_window.withdraw()



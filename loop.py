from tkinter import *
import sqlite3 as db
from add_car import push_car
from prettytable import PrettyTable

connect = db.connect("C:/projects/autoru/auto_db.db")
cursor = connect.cursor()


# val = input("Sort by:\n1 - valid WIN\n2 - Price\n3 - Reg year\n4 - Mileage\n5 - None\n-> ")


def cars_by_price():
    output_window = Tk()
    output_window.title("NEauto.ru (Car list, Price)")
    output_window.geometry("900x800")
    scb = Scrollbar(output_window)
    t_out = Text(output_window, height=800, width=900, yscrollcommand=scb.set)
    th = ["Brand", "Model", "VIN", "Valid_VIN", "Mileage", "Registration Year", "Price"]
    td = []
    for i in cursor.execute("""SELECT * FROM cars ORDER BY price"""):
        for j in i:
            td.append(j)
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    t_out.insert(END, table)
    scb.pack(side=RIGHT, fill=Y)
    t_out.pack()


def cars_by_val_win():
    output_window = Tk()
    output_window.title("NEauto.ru (Car list, Valid WIN)")
    output_window.geometry("900x800")
    scb = Scrollbar(output_window)
    t_out = Text(output_window, height=800, width=900, yscrollcommand=scb.set)
    th = ["Brand", "Model", "VIN", "Valid_VIN", "Mileage", "Registration Year", "Price"]
    td = []
    for i in cursor.execute("""SELECT * FROM cars ORDER BY valid_win"""):
        for j in i:
            td.append(j)
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    t_out.insert(END, table)
    scb.pack(side=RIGHT, fill=Y)
    t_out.pack()


def cars_by_mileage():
    output_window = Tk()
    output_window.title("NEauto.ru (Car list, Mileage)")
    output_window.geometry("900x800")
    scb = Scrollbar(output_window)
    t_out = Text(output_window, height=800, width=900, yscrollcommand=scb.set)
    th = ["Brand", "Model", "VIN", "Valid_VIN", "Mileage", "Registration Year", "Price"]
    td = []
    for i in cursor.execute("""SELECT * FROM cars ORDER BY mileage"""):
        for j in i:
            td.append(j)
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    t_out.insert(END, table)
    scb.pack(side=RIGHT, fill=Y)
    t_out.pack()


def cars_by_reg_year():
    output_window = Tk()
    output_window.title("NEauto.ru (Car list, Registration year)")
    output_window.geometry("900x800")
    scb = Scrollbar(output_window)
    t_out = Text(output_window, height=800, width=900, yscrollcommand=scb.set)
    th = ["Brand", "Model", "VIN", "Valid_VIN", "Mileage", "Registration Year", "Price"]
    td = []
    for i in cursor.execute("""SELECT * FROM cars ORDER BY reg_year"""):
        for j in i:
            td.append(j)
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    t_out.insert(END, table)
    scb.pack(side=RIGHT, fill=Y)
    t_out.pack()


def cars_by_brand():
    output_window = Tk()
    output_window.title("NEauto.ru (Car list, Brand)")
    output_window.geometry("900x800")
    scb = Scrollbar(output_window)
    t_out = Text(output_window, height=800, width=900, yscrollcommand=scb.set)
    th = ["Brand", "Model", "VIN", "Valid_VIN", "Mileage", "Registration Year", "Price"]
    td = []
    for i in cursor.execute("""SELECT * FROM cars ORDER BY brand"""):
        for j in i:
            td.append(j)
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    t_out.insert(END, table)
    scb.pack(side=RIGHT, fill=Y)
    t_out.pack()


def cars_by_none():
    output_window = Tk()
    output_window.title("NEauto.ru (Car list, none)")
    output_window.geometry("900x800")
    scb = Scrollbar(output_window)
    t_out = Text(output_window, height=800, width=900, yscrollcommand=scb.set)
    th = ["Brand", "Model", "VIN", "Valid_VIN", "Mileage", "Registration Year", "Price"]
    td = []
    for i in cursor.execute("""SELECT * FROM cars"""):
        for j in i:
            td.append(j)
    columns = len(th)
    table = PrettyTable(th)
    td_data = td[:]
    while td_data:
        table.add_row(td_data[:columns])
        td_data = td_data[columns:]
    t_out.insert(END, table)
    scb.pack(side=RIGHT, fill=Y)
    t_out.pack()


def run_print_loop():
    print_loop = Tk("Car list")
    print_loop.title("NEauto.ru (Car list)")
    print_loop.geometry("400x400")
    lb_text = Label(print_loop, text="Sorted by:", width=15, height=1, font="Arial 16")

    btn_brand = Button(print_loop, text="Brand", width=15, height=2, font="Arial 14", command=cars_by_brand)
    btn_val_win = Button(print_loop, text="Valid WIN", width=15, height=2, font="Arial 14", command=cars_by_val_win)
    btn_price = Button(print_loop, text="Price", width=15, height=2, font="Arial 14", command=cars_by_price)
    btn_reg_year = Button(print_loop, text="Registration year", width=15, height=2, font="Arial 14",
                          command=cars_by_reg_year)
    btn_mileage = Button(print_loop, text="Mileage", width=15, height=2, font="Arial 14", command=cars_by_mileage)
    btn_none = Button(print_loop, text="None", width=15, height=2, font="Arial 14", command=cars_by_none)

    lb_text.pack()
    btn_brand.pack()
    btn_val_win.pack()
    btn_price.pack()
    btn_reg_year.pack()
    btn_mileage.pack()
    btn_none.pack()


def add_car_loop():
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

    for row in cursor.execute("""SELECT * FROM wins win"""):
        for i in row:
            if i == win:
                valid_win = "True"
    btn_add = Button(add_car_window, text="Add", width=10, height=1, font="Arial 14",
                     command=push_car1(brand, model, win, valid_win, mileage, reg_year, price)).grid(row=6, column=1)


def push_car1(brand, model, win, valid_win, mileage, reg_year, price):
    req = "INSERT INTO cars VALUES ('" + brand.get() + "', '" + model.get() + "', '" + win.get() + "',  '" + valid_win + "', '" + mileage.get() + "', '" + reg_year.get() + "', '" + price.get() + "')"
    cursor.execute(req)
    connect.commit()


def loop():
    master_window = Tk("Master")
    master_window.title("NEauto.ru (Main menu)")
    master_window.geometry("400x300")
    lb_main = Label(master_window, text="NEauto.ru", width=10, height=1, font="Arial 18")
    btn_print = Button(master_window, text="Car list", width=20, height=3, font="Arial 14", command=run_print_loop)
    btn_add = Button(master_window, text="Add car", width=20, height=3, font="Arial 14", command=push_car)
    btn_exit = Button(master_window, text="Exit", width=20, height=3, font="Arial 14", command=exit)

    lb_main.pack()
    btn_print.pack()
    btn_add.pack()
    btn_exit.pack()

    mainloop()

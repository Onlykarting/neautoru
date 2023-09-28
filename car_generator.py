import random as rn
import sqlite3 as db
from win_generator import win_generate_to_car

connect = db.connect("C:/projects/autoru/auto_db.db")
cursor = connect.cursor()


def list_to_str(arr):
    ans = ""
    for i in arr:
        ans += str(i)
    return ans


def car_create():
    brands = ["BMW", "Mercedes", "Volkswagen", "Toyota", "Subaru", "Nissan", "Skoda", "Audi", "Land Rover", "Hyundai",
              "Range Rover", "Porsche"]
    bmw_abc = ["X1", "X3", "X5", "X6", "320i", "M5", "Z4", "M8", "X2"]
    mercedes_abc = ["GLA", "GLE", "GLC", "G63", "Vivano", "CLA", "ML", "GLB"]
    volkswagen_abc = ["Passat", "Tiguan", "Touareg", "Polo", "Golf", "Amarok", "Jetta", "Teramont", "Scirocco"]
    toyota_abc = ["Camry", "Corolla", "C-HR", "Hilux", "RAV4", "Mark 2", "Yaris", "GT86", "Celica"]
    subaru_abc = ["IMPREZA", "FORESTER", "LEGACY", "BRZ", "OUTBACK", "IMPREZA WRX", "IMPREZA WRX STI", "FORESTER STI",
                  "SVX"]
    nissan_abc = ["Patrol", "Juke", "Almera", "Murano", "Skyline", "X-Trail", "Tiida", "350Z", "370Z", "Silvia"]
    skoda_abc = ["Rapid", "Octavia", "Superb", "Scout", "KODIAQ", "Fabia"]
    audi_abc = ["TT", "Q7", "RS3", "A1", "A2", "A3", "S3", "S5"]
    land_rover_abc = ["Discovery", "Defender", "Freelender"]
    range_rover_abc = ["Sport", "Velar", "Evoque"]
    huundai_abc = ["Accent", "Creta", "Getz", "Lantra", "Solaris", "Sonata", "Coupe"]
    prosche_abc = ["911", "918", "Panamera", "Cayman", "Cayenne", "Macan"]

    brand = ""
    model = ""
    vin = ""
    mileage = ""
    reg_year = ""
    price = ""

    brand = rn.choice(brands)
    if brand == "BMW":
        model = rn.choice(bmw_abc)
    elif brand == "Mercedes":
        model = rn.choice(mercedes_abc)
    elif brand == "Volkswagen":
        model = rn.choice(volkswagen_abc)
    elif brand == "Toyota":
        model = rn.choice(toyota_abc)
    elif brand == "Subaru":
        model = rn.choice(subaru_abc)
    elif brand == "Nissan":
        model = rn.choice(nissan_abc)
    elif brand == "Skoda":
        model = rn.choice(skoda_abc)
    elif brand == "Audi":
        model = rn.choice(audi_abc)
    elif brand == "Land Rover":
        model = rn.choice(land_rover_abc)
    elif brand == "Hyundai":
        model = rn.choice(huundai_abc)
    elif brand == "Range Rover":
        model = rn.choice(range_rover_abc)
    elif brand == "Porsche":
        model = rn.choice(prosche_abc)
    vin = win_generate_to_car()
    mileage = str(rn.randint(0, 300000))
    reg_year = str(rn.randint(2010, 2022))
    price = str(rn.randint(500000, 7000000))
    valid_vin = "True"
    return str(
        "INSERT INTO cars VALUES ('" + brand + "', '" + model + "', '" + vin + "',  '" + valid_vin + "', '" + mileage + "', '" + reg_year + "', '" + price + "')")


def car_generate(num):
    for i in range(num):
        car = car_create()
        cursor.execute(car)
        connect.commit()
    return True

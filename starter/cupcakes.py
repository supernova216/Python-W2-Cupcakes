from abc import ABC, abstractmethod
from pprint import pprint
import csv

class Cupcake(ABC):
    def __init__(self,name,price,flavor,frosting,filling):
        size = "Regular"
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
    
    def add_sprinkles(self,*args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self,quantity):
        return quantity*self.price
    
class Mini(Cupcake):
    size = "Mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
    
    def calculate_price(self, quantity):
        return quantity*self.price
    
class Regular(Cupcake):
    size = "Regular"

    def calculate_price(self, quantity):
        return quantity*self.price

class Large(Cupcake):
    size = "Large"

    def calculate_price(self, quantity):
        return quantity*self.price

cupcake1 = Large("Freedom",4.99,"Vanilla","Vanilla","Strawberry")
cupcake1.add_sprinkles("Red","White","Blue")
cupcake2 = Mini("Berry Fun",2.99,"Strawberry","Strawberry")
cupcake2.add_sprinkles("Red")
cupcake3 = Regular("Death by Chocolate",3.99,"Chocolate","Chocolate","Fudge")
cupcake3.add_sprinkles("Brown")
cupcake4 = Mini("Freedom",2.99,"Vanilla","Vanilla")
cupcake4.add_sprinkles("Red","White","Blue")
cupcake5 = Regular("Freedom",3.99,"Vanilla","Vanilla","Strawberry")
cupcake5.add_sprinkles("Red","White","Blue")
cupcake6 = Regular("Berry Fun",3.99,"Strawberry","Strawberry","Vanilla")
cupcake6.add_sprinkles("Red")
cupcake7 = Large("Berry Fun",4.99,"Strawberry","Strawberry","Vanilla")
cupcake7.add_sprinkles("Red")
cupcake8 = Mini("Death by Chocolate",2.99,"Chocolate","Chocolate")
cupcake8.add_sprinkles("Brown")
cupcake9 = Large("Death by Chocolate",4.99,"Chocolate","Chocolate","Fudge")
cupcake9.add_sprinkles("Brown")

def readcsv(file):
    with open(file) as csvfile: 
        reader = csv.DictReader(csvfile)
    
        for row in reader:
            pprint(row)

readcsv("sample.csv")


cupcake_list = [cupcake1,cupcake2,cupcake3]
store_list = [cupcake1,cupcake2,cupcake3,cupcake4,cupcake5,cupcake6,cupcake7,cupcake8,cupcake9]
order_list = [cupcake9,cupcake2,cupcake5]

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake,"filling"):
                writer.writerow({"size":cupcake.size,"name":cupcake.name,"price":cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting,"filling":cupcake.filling})
            else:
                writer.writerow({"size":cupcake.size,"name":cupcake.name,"price":cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting})

write_new_csv("sample.csv",cupcake_list)
write_new_csv("store.csv",store_list)
write_new_csv("order.csv",order_list)

def add_cupcake(file,cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size","name","price","flavor","frosting","sprinkles","filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        if hasattr(cupcake,"filling"):
            writer.writerow({"size":cupcake.size,"name":cupcake.name,"price":cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting,"filling":cupcake.filling})
        else:
            writer.writerow({"size":cupcake.size,"name":cupcake.name,"price":cupcake.price,"flavor":cupcake.flavor,"frosting":cupcake.frosting})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)
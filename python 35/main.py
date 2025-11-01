listi = [(1, 3), (4, 2), (2, 5)]
sorted_listi = sorted( listi, key=lambda x : x[1] )
print(sorted_listi)


import random

def moqmedi_sia(raodenoba, minimum, maksimum):
    try:
        sia = [random.randint(minimum, maksimum) for _ in range(raodenoba)]
        print(" სიაა:", sia)
        monacemebi = input("შეიყვანე ინდექსი " + str(len(sia)-1) + "მდე: ")
        try:
            monacemebi = int(monacemebi)
            if monacemebi < 0 or monacemebi >= len(sia):
                print("ასეთი ინდექსი არ არსებობს სიაში!")
            else:
                print("ინდექსზე", monacemebi, " ელემენტი:", sia[monacemebi])

        except ValueError:
            print(" ინდექსი უნდა იყოს რიცხვი!")

    except Exception as shecdoma:
        print("ზოგადი შეცდომა: ", shecdoma)
moqmedi_sia(10, 8,20)


products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

fasi = list (filter(lambda x: x["price"] > 100, products))
print(" ფასი მეტია 100ზე: ", fasi)

saxelebi = list(map(lambda x : (x["name"], x ["price"]), products))
print("სახელები და ფასები: ", saxelebi)

sorted_products = sorted ( products, key = lambda x: x["price"])
print("ფასების მიხედვით დასორტირებული: ", sorted_products)

from functools import reduce
total_price = reduce(lambda jami, element: jami + element["price"], products, 0)
print("სულ ფასი: ", total_price)


def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)
print(recursive_sum(9))


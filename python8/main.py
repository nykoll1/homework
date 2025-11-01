numbers = { i: i**2 for i in range(1,11)}
print(numbers)


products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10}},
    {"fanta": {
        "price": 2.5,
        "quantity": 5}},
    {"snickers": {
        "price": 3.5,
        "quantity": 12}},
    {"water": {
        "price": 4.5,
        "quantity": 8}},
    {"beer": {
        "price": 6.5,
        "quantity": 5}}
]
print("პროდუქტების დასახელება: ")
for i in products:
    for name in i.keys():
        print(name)
jam = 0
for i in products:
    for name in i:
        jam = jam + i [name]["price"] * i [name]["quantity"]
print("პროდიქტის ღირებულების ჯამია: ", jam)


fruits = {}
name = ""
while name != "stop":
    name = input("შეიყვანეთ თქვენი საყვარელი ხილი: ")
    if name != "stop":
        if name in fruits:
            fruits[name] = fruits[name] + 1
        else:
            fruits[name] = 1

print(fruits)
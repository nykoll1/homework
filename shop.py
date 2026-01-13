from pymongo import MongoClient
import random
client = MongoClient("mongodb://localhost:27017/")
db = client["shop"]
products_collection = db["products"]

categories = ["Electronics", "Books", "Clothes"]
products = []
for i in range(1, 51):
    quantity = random.randint(0, 100)

    product = {
        "name": f"Product {i}",
        "category": random.choice(categories),
        "price": random.randint(50, 3000),
        "quantity": quantity,
        "available": False if quantity == 0 else True
    }
    products.append(product)


products_collection.insert_many(products)
print(" ყველა პროდუქტი:")
for p in products_collection.find():
    print(p)

print("\n ხელმისაწვდომი პროდუქტები:")
for p in products_collection.find({"available": True}):
    print(p)

print("\n პროდუქტები ფასით > 1000:")
for p in products_collection.find({"price": {"$gt": 1000}}):
    print(p)

print("\nპროდუქტების რაოდენობა კატეგორიების მიხედვით:")
categories = ["Electronics", "Books", "Clothes"]
for category in categories:
    count = products_collection.count_documents({"category": category})
    print(category, count)

products_collection.update_one(
    {"name": "Product 1"}, {"$set": {"quantity": 25, "available": True}}
)

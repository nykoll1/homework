from faker import Faker
import json
import random

fake = Faker()
students = []

for _ in range(100):
    student = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False])
    }
    students.append(student)
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    data = json.load(file)
active_students = [s for s in data if s["is_active"] is True]
with open("active_students.json", "w") as file:
    json.dump(active_students, file, indent=4)

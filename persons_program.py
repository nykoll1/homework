import json

def add_persons(n):
    with open("persons.json", "r") as f:
        persons = json.load(f)

   
    if persons:
        last_id = persons[-1]["id"]
    else:
        last_id = 0

   
    for _ in range(n):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        last_id += 1  

        new_person = {
            "id": last_id,
            "name": name,
            "age": age
        }

        persons.append(new_person)
    with open("persons.json", "w") as f:
        json.dump(persons, f, indent=4)

add_persons(2)
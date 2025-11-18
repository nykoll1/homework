class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def serialize(person):
    return f"Name: {person.name}, Age: {person.age}"
def deserialize(text_line):
    parts = text_line.split(",")   
    name = parts[0].split(":")[1].strip()
    age = int(parts[1].split(":")[1].strip())
    return Person(name, age)

p1 = Person("Otar", 34)

with open("person.txt", "w") as file:
    file.write(serialize(p1))

with open("person.txt", "r") as file:
    line = file.readline()
    restored = deserialize(line)
print(f"Name: {restored.name}, Age: {restored.age}")

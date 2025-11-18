class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"
def serialize(person):
    return f"Name: {person.name}, Age: {person.age}"

def deserialize(text_line):
    
    parts = text_line.split(",")  
    name_part = parts[0].split(":")[1].strip() 
    age_part = parts[1].split(":")[1].strip()   

    return Person(name_part, int(age_part))  

p1 = Person("Otar", 34)
serialized = serialize(p1)

f = open("person.txt", "w")
f.write(serialized)
f.close()
f = open("person.txt", "r")
line = f.readline()
f.close()
new_person = deserialize(line)

print(new_person)
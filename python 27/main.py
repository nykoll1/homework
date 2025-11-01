persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]
name = ""

while name != "stop":
    name = input("შეიყვანეთ სახელი ან დაწერეთ 'stop': ").strip()
    if name.lower() == "stop":
        break

    name = name.capitalize()
    i = 0
    while i < len(persons):
        if name == persons[i][0]:
            break
        i += 1

    if i == len(persons):
        print("ასეთი სახელი სიაში არ არის.")
        continue


    surname = input("შეიყვანეთ გვარი: ").strip()
    surname = surname.capitalize()
    i = 0
    while i < len(persons):
        if surname == persons[i][1]:
            break
        i += 1
    if i == len(persons):
        print("ასეთი გვარი სიაში არ არის.")
        continue
    i = 0
    while i < len(persons):
        if name == persons[i][0] and surname == persons[i][1]:
            print("ასაკი არის:", persons[i][2])
            break
        i += 1

    if i == len(persons):
        print("ასეთი ადამიანი სიაში არ არის.")

word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")
set1 = set(word1)
set2 = set(word2)

saerto = set1 & set2     
gansxvavebuli = set1 ^ set2     
gaertianeba = set1 | set2   
print("საერთო სიმბოლოები:", saerto)
print("განსხვავებული სიმბოლოები:", gansxvavebuli)
print("გაერთიანებული სიმბოლოები:", gaertianeba)
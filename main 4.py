import random

print("გამოიცანი რიცხვი 1-დან 100-მდე. გაქვს 5 ქულა.")
points = 5
for i in range(5):
    user = int(input("შეიყვანე რიცხვი: "))
    number = random.randint(1, 100)  

    if user == number:
        print("გილოცავ! სწორად გამოიცანი ")
        print("დაგრჩა ქულა:", points)
        break
    elif user < number:
        points -= 1
        print("შენი რიცხვი მეტია!")
        print("დაგრჩა ქულა:", points)
    else:
        points -= 1
        print("შენი რიცხვი ნაკლებია!")
        print("დაგრჩა ქულა:", points)

else:
    print(" ვერ გამოიცანი ")
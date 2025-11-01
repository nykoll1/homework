ricxvebi =[ 7, 9, 12, 9, 12]
print("რიცხვებია", ricxvebi)
jam = 0
for r in ricxvebi:
    jam += r
sashualo = jam/len(ricxvebi)
print("რიცხვების ჯამი არის:", jam)
print("რიცხვების საშუალო არის:", sashualo)

mixed_list = ["a", "b", 2, 4, 2, "c", "j",1, "b", "d", "c", 4, 1]
new_list = []
for i in mixed_list:
    if i not in new_list:
        new_list.append(i)
print("ახალი სია:", new_list)


import random
nums = []
nums = [random.randint(-50, 50) for i in range(20)] 
print("მთლიანი სია:", nums)

num_list= []
num_list= [num for num in nums  if num %2 == 0]
print("ლუწი რიცხვები", num_list)


long_names = []
short_names = []
name = ""  

while name != "stop":  
    name = input("შეიყვანეთ სახელი ან დაწერეთ 'stop' დასასრულებლად: ")
    if name == "stop":
        break
    name= name.capitalize()
    
    if len(name) > 3:
        long_names.append(name)
        print(name, "დაემატა გრძელი სახელების სიაში")
    else:
        short_names.append(name)
        print(name, "დაემატა მოკლე სახელების სიაში")
print("გრძელი სახელები:", long_names)
print("მოკლე სახელები:", short_names)
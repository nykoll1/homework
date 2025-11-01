wona = float(input("შეიყვანეთ თქვენი წონა : "))
simagle= float(input("შეიყვანეთ თქვენი სიმაღლე მეტრებში (მაგ: 1.75): "))
BMI = wona / (simagle **2 )
if BMI < 19 :
    print("underweight")
elif BMI >=19 and BMI<=25 :
    print("normalweight")
else:
    print( "overwight")   


a= int(input("შეიყვანეთ პირველი რიცხვი"))
b= int(input("შეიყვანეთ მეორე რიცხვი"))
c = input("შეიყვანეთ არითმეტიკული ოპერატორი")
if c == "+":
    print(a + b)
elif c == "-" :
    print (a-b)
elif c == "*" :
    print (a*b)
elif c == "/":
    print
    if b !=0:
        print(a/b)
    else:
        print( "0-ზე გაყოფა შეუძლებელია")
else:
    print("არასწორია")

num1= int(input("შეიყვანეთ პირველი რიცხვი:"))
num2 = int(input("შეიყვანეთ მეორე რიცხვი:"))
num3= int(input("შეიყვანეთ მესამე რიცხვი"))
if num1==num2==num3:
    print("შეიყვანეთ განსხვავებული რიცხვი")
elif num1==num2 :
    print("შეიყვანეთ განსხვავებული რიცხვი")
elif num1==num3 :
     print("შეიყვანეთ განსხვავებული რიცხვი")
elif num2==num3 :
     print("შეიყვანეთ განსხვავებული რიცხვი")
else:
    if num1> num2 and num1> num3:
        print("ყველაზე დიდი რიცხვია:", num1)
    elif num2> num1 and num2 >num3:
         print("ყველაზე დიდი რიცხვია:", num2)   
    else:
        print("ყველაზე დიდი რიცხვია:", num3)
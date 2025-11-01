def sum_numbers ( raodenoba = 5):
    total = 0
    for i in range (raodenoba):
        num= int (input( "შეიყვანე რიცხვი: "))
        total += num
    print( "რიცხვების ჯამი: " , total)
    return total
sum_numbers(3)



def number(*args):
    even = []
    odd = []

    for m in args:
        if m % 2 == 0:
            even.append(m)
        else:
            odd.append(m)
    print( "ლუწი რიცხვებია:", even)
    print( " კენტი რიცხვებია:", odd)
    return even , odd
number( *range (1, 101))
        
 

def word_frequency(text):
    text= text.lower()
    words= text.split()
    sitkva ={}

    for n in words:
        if n in sitkva:
            sitkva[n] +=1
        else:
            sitkva[n] = 1
    return sitkva
sentence = input("შეიყვანეთ წინადადება: ")
result = word_frequency(sentence)
print("სიტყვების რაოდენობა:" , result)


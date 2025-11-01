sentence = input("შეიყვანეთ წინადადება: ")
words = sentence.split()
if len(words) >= 2:
    words[0], words[1] = words[1], words[0]
    print("შედეგი", end = " ")
    for i in range (len(words)):
        print(words[i], end = "")
        if i < len(words) -1 :
            print( " ", end= "" )
else:
    print("შეიყვანეთ ორ სიტყვიანი წინადადება")


   
sentence = input("შეიყვანეთ წინადადება:")
words = sentence.split()

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("ყველაზე გრძელი სიტყვაა:", longest)


w1 = input("შეიყვანეთ პირველი სიტყვა: ") .lower()
w2 = input("შეიყვანეთ მეორე სიტყვა: ").lower()
if len(w1) != len(w2):
    print("ეს სიტყვები ანაგრამები არ არის")
else:
    same_letters =0   
    for i in w1:
        if i in w2:
            same_letters = same_letters + 1
    if same_letters == len(w1):
        print("ეს სიტყვები ანაგრამებია")
    else:
        print("ეს სიტყვები ანაგრამები არ არისს")
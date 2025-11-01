def check_text(text):
    didi = 0
    for i in text:
        if "A" <= i <= "Z":
            didi += 1
    big_text = text.upper()

    return f"დიდი ასოების რაოდენობა: {didi} \n ტექსტი დიდი ასოებით: {big_text}"
text = input("შეიყვანე ტექსტი: ")
print(check_text(text))


def snake_camel(text):
    if "_" in text:
        snake_case = text.split("_")        
        camel_case = snake_case[0]          
        for word in snake_case[1:]:         
            camel_case += word.capitalize()
        return camel_case
    
    else:
        camel_case = text
        snake_case = ""
        for n in camel_case:
            if n.isupper():
                snake_case += "_" + n.lower()
            else:
                snake_case += n
        return snake_case
momxmarebeli = input("შეიყვანე ტექსტი (snake_case ან camelCase): ")
result = snake_camel(momxmarebeli)

print("შედეგი:", result)

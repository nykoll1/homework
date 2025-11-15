def commission(func):
    def wrapper(balance, amount):
        if balance < 1:
            return "ანგარიშზე საკომისიო თანხა არ არის"
        balance -= 1
        return func(balance, amount)

    return wrapper
@commission
def transfer(balance, amount):
    
    if balance < amount:
        return "ანგარიშზე არასაკმარისი თანხაა!"
    balance -= amount
    return f"ტრანსაქცია წარმატებით შესრულდა. დარჩენილი ბალანსი: {balance}"

print(transfer(20, 5))



class MethodNameValidator(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value):      
                if not key.startswith("_"):
                    raise ValueError(f"მეთოდი '{key}' უნდა იწყებოდეს '_' -თი")
        return super().__new__(cls, name, bases, attrs)

class OK(metaclass=MethodNameValidator):
    age = 20
    country = "Geo"
    def _hello(self):
        return "hi"
    def _calc(self):
        return 12 + 5

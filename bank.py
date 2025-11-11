class BankSystem:
    bank_name = "TBC Bank"            
    __total_accounts = 0               

    def __init__(self, owner, balance):
        self._owner = owner            
        self.__balance = balance       
        BankSystem.__total_accounts += 1
        self.__account_number = f"{BankSystem.__total_accounts}"  

    def deposit(self, amount):
        if BankSystem.validate_amount(amount):
            self.__balance += amount
            print(f"{amount} დამატებულია ანგარიშზე")
        else:
            print("შეიყვანე სწორი თანხა")

    def withdraw(self, amount):
        if BankSystem.validate_amount(amount) and self.__balance >= amount:
            self.__balance -= amount
            print(f"{amount}  გამოტანილია ანგარიშიდან.")
        else:
            print("შეუძლებელია ოპერაციის შესრულება!")

    def check_balance(self):
        print(f"ბალანსი: {self.__balance} ")
    def get_account_number(self):
        return self.__account_number
    def change_owner(self, new_owner):
        self._owner = new_owner
        print(f"ანგარიშის მფლობელი შეიცვალა: {new_owner}")

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts
    
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0
    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"

acc1 = BankSystem("Nino Beridze", 500)
acc2 = BankSystem("Giorgi Kapanadze", 1200)

print(acc1)
print(acc2)
acc1.deposit(200)
acc1.withdraw(100)
acc1.check_balance()
acc2.withdraw(500)
acc2.change_owner("Nika Chitadze")
print(f"სულ ანგარიშებია გახსნილი: {BankSystem.get_total_accounts()}")
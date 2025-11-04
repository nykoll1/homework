class Student:
    status = True
    pay = 1000

    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades  

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    def get_discount(self):
        if self.age < 18:
            self.pay = self.pay * 0.8  
        return self.pay
    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
    def get_status(self):
        average = self.calculate_average()

        if average >= 90:
            result = "Excellent"
        elif 70 <= average < 90:
            result = "Good"
        elif 50 <= average < 70:
            result = "Average"
        else:
            result = "Poor"
            self.status = False  
        return result
    
student1 = Student("Nika", "Chitadze", 17, [15, 45, 83])
print(" სახელი: ", student1.get_full_name())
print("საშუალო ქულა: ", student1.calculate_average())
print("სტატუსი: ", student1.get_status())
print("გადასახადი: ", student1.get_discount())
print("მდგომარეობა: ", student1.status)
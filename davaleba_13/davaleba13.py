# davaleba 1

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > 0 and self.balance <= amount:
            print(f"Oops! {self.account_holder}, you don't have enough balance. Your current balance is: {self.balance}. Maximum withdrawal is: {self.balance}.")
        elif amount < 0:
            print("Withdrawal must be positive.")


person_1 = BankAccount('012345678901', 'Jack Richer', 25)
person_2 = BankAccount('012345678902', 'Bob Marley', 99999)
person_3 = BankAccount('012345678903', 'Anna Holloway', 98765)

person_1.withdraw(100)
person_2.withdraw(100)
person_3.withdraw(2100)
person_1.deposit(100)
person_1.deposit(20000)
print(f"{person_1.account_holder}: {person_1.balance}")
print(f"{person_2.account_holder}: {person_2.balance}")
print(f"{person_3.account_holder}: {person_3.balance}")

# davaleba 2

class Student:
    def __init__(self, first_name, last_name, student_id, courses):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.courses = courses
    def add_course(self, new_course):
        self.courses.append(new_course)
    def show_courses(self):
        print(f"{self.first_name} {self.last_name}-ს (პ.ნ. - {self.student_id}) კურსები: {self.courses}")
    def show_courses_quantity(self):
        print(f"{self.first_name} {self.last_name}-ს (პ.ნ. - {self.student_id}) კურსების რაოდენობა: {len(self.courses)}")

student_1 = Student("Nika", "Davitashvili", "01011109876", ["ვებ პროგრამირება (Front End Development)", "ალბათობის თეორია და მათემატიკური სტატისტიკა", "მონაცემთა სტრუქტურები და ალგორითმები", "კომპიუტერის სისტემური პროგრამები", "მონაცემთა ანალიტიკა (Python)"])
student_2 = Student("Ana", "Zaridze", "15003245122", ["კალკულუსი", "Python საწყისები", "მეწარმეობა", "მენეჯმენტის საფუძვლები", "ოპერაციული მენეჯმენტი"])
student_3 = Student("Dima", "Oboladze", "01010101011", ["ჯანსაღი კვება", "შესავალი მწვრთელობაში", "საუბრის ტექნიკა", "ანალიტიკა", "პირველადი დახმარება"])


student_1.add_course("IT-Step-Python-Django")
student_3.add_course("კომენტატორობა")
student_2.add_course("ციფრული ტექნოლოგიები")
student_1.show_courses_quantity()
student_1.show_courses()
student_2.show_courses_quantity()
student_2.show_courses()
student_3.show_courses_quantity()
student_3.show_courses()

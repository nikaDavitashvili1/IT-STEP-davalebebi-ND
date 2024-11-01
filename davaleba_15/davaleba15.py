class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner, status="onsale"):
        if not isinstance(owner, Person):
            raise ValueError("owner must be a Person object")
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell(self, buyer, loan_amount=None):
        if loan_amount is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold"
        else:
            self.owner.deposit += self.price
            buyer.loan += loan_amount
            self.owner = buyer
            self.status = "sold on loan"

    def __str__(self):
        return f"ID: {self.ID}, Price: {self.price}, Owner - {self.owner}, Status: {self.status}"

person1 = Person("Mr. Bean")
print(person1.__str__())
person2 = Person("Roboto")
print(person2.__str__())
house = House(39868099, 150000, owner=person1)
print(house.__str__())
print("\nAfter Selling The house:")
house.sell(person2)
print(person1.__str__())
print(person2.__str__())
print(house.__str__())

print("\nAfter Selling The house w loan:")
house.sell(person1, 20000)
print(person1.__str__())
print(person2.__str__())
print(house.__str__())


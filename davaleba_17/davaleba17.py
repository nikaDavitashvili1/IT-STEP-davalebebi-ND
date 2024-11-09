
class Node:  #ვქმნით ნოუდ კლასს (თავიდან უნდა იყოს ცარიელი, რომ მნიშვნელობები ჩვენ მივანიჭოთ (data=None)):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList: #ვქმნით ბმული სიის კლასს:
    def __init__(self):
        self.head = None

    def append(self, data): #აღვწეროთ ეფენდ მეთოდი:
        new_node = Node(data) #შევქმნათ ახალი ნოუდი;
        if self.head is None: #თუ სია ცარიელია, პირველი ნოუდი არის ჰედი;
            self.head = new_node
            return

        last_node = self.head #შემოვიტანოთ ახალი ცვლადი - ლასთნოუდი ლოგიკის დასაწერად;
        while last_node.next: #სანამ შემდეგი ელემენტი არსებობს, გადავიდეს ამ ელემენტზე, რომ გავიდეთ სიის ბოლოში;
            last_node = last_node.next

        last_node.next = new_node #გავედით ბოლოში და ბოლოს შემდეგ ვქმნით ახალს.

    def remove_value(self, value): # ვქმნით მეთოდს მნიშვნელობით წასაშლელად
        current_node = self.head
        prev_node = None

        while current_node is not None:
            if current_node.data == value:
                if prev_node is None:  # თუ წასაშლელი ელემენტი ჰედია
                    self.head = current_node.next
                else:  # სხვა შემთხვევაში, წინა ელემენტი გადაამოწმოს შემდეგით
                    prev_node.next = current_node.next
                return  # ვპოულობთ და ვწყვეტთ მუშაობას, რადგან მხოლოდ პირველ თავსებად ელემენტს ვშლით
            prev_node = current_node
            current_node = current_node.next

    def insert_at(self, index, data):  # ვქმნით მეთოდს ელემენტის დასამატებლად ინდექსით
        new_node = Node(data)

        if index == 0:  # თუ პირველი ინდექსია, მაშინ ახლად შექმნილი ნოუდი ჰედზე მოათავსოს
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_position = 0

        while current_node is not None and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node is None:
            print("Index out of bounds")
            return

        new_node.next = current_node.next
        current_node.next = new_node

    def remove_at(self, index): #შევქმნათ ახალი, ინდექსით წაშლის მეთოდი
        if index < 0 and self.head is None: #თუ სია ცარიელია, რომ არ დაგვიეროროს
            return

        if index == 0: #თუ პირველივე ელემენტს ვშლით, შეიცვალოს მისი მნიშვნელობა მის მარჯვნივ მდგომი ელემენტის მნიშვნელობით.
            self.head = self.head.next
            return

        current_node = self.head #შევქმნათ ახალი ცვლადი ქარენთ ნოუდი ლოგიკის დასაწერად
        current_position = 0 #და ინდექსის ცვლადიც რა თქმა უნდა

        while current_node.next and current_position < index - 1: #ვიპოვოთ მოთხოვნილი ნოუდის ინდექსი სად მდებარეობს:
            current_node = current_node.next
            current_position += 1

        if current_node.next: #დავამატოთ წაშლის მეთოდი:
            current_node.next = current_node.next.next

    def display(self): #დავამატოთ ლისტის დაპრინტვის მეთოდი, რომ ობიექტი არ დაგვიპრინტოს
        current_node = self.head #დავიჭიროთ პირველივე ელემენტი, რომ მაქედან დავიწყოთ დაპრინტვა
        while current_node is not None: #სანამ სია არსებობს:
            print(current_node.data, end=' -> ') #ნოუდში რა დატაც არის ის ამოპრინტოს და ისარიც მიუწეროს გვერდზე :)
            current_node = current_node.next #გადავიდეს შემდეგ ელემენტზე.

'''დაწერეთ value გადაწოდების შედეგად ამოშლის ლოგიკა დაკავშირებულ სიებში და ინდექსით ჩამატების ლოგიკა'''


# მაგალითები
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(5)
linked_list.append(25)
linked_list.append(12)
linked_list.append(11)

linked_list.display()
print()
linked_list.remove_at(2)
linked_list.display()
print()
linked_list.remove_at(2)
linked_list.insert_at(1, "orasii")
linked_list.remove_value(10)
linked_list.display()

# stekis kodi (Node-s aghar gadmovitan barem, radgan igive klasia)

class Stack: #შევქმათ ახალი კლასი - სტეკი:
    def __init__(self): #აღვუწეროთ ატრიბუტები - პირველი ნოუდი, რომელიც ჯერ ცარიელია, და სტეკის სიგრძე, რომელიც თავიდან ასევე 0-ია.
        self.top_node = None
        self.length = 0

    def empty(self): #სიცარიელის შემოწმების მეთოდი
        return self.length == 0

    def size(self): #სიგრძის შემოწმების მეთოდი
        return self.length

    def push(self, data): #ახალი ნოუდის ჩამატების მეთოდი (ცალი მხრიდან)
        new_node = Node(data) #ახალი ნოუდისთვის ვქმნით ცვლადს ნიუ_ნოუდ
        new_node.next = self.top_node #ახალი ნოუდის გვერდით მდგომი გახდეს ჰედი, პირველი ელემენტი
        self.top_node = new_node #ჰედი გახდეს ახალი ნოუდი
        self.length += 1 #სიგრძე იზრდება ერთით

    def pop(self): #ტოპ ნოუდის წაშლის და გამოტანის მეთოდი
        if not self.empty(): #ამოქმედდეს ლოგიკა თუ ცარიელი არაა სია.
            popped_item = self.top_node.data # ახალი ცვლადი წასაშლელი ინფორმაციის დასაბეჭდად
            self.top_node = self.top_node.next # ტოპ ნოუდი წაიშალოს და, ამასთან, მის გვერდით მდგომი გახდეს ტოპნოუდი
            self.length -= 1 # წაიშალა ელემენტი, დაიკლო ზომამ
            return popped_item  #დაგვიპრინტოს დამახსოვრებული ცვლადის მნიშვნელობა
        else: #თუ ცარიელია, ინდექსის ერორი:
            raise IndexError('Stack is empty')

print("\n")
#მაგალითები

stack = Stack()
# print(stack.empty())
# print(stack.size())

stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)
# print(stack.empty())
# print(stack.size())


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.empty())
# print(stack.size())

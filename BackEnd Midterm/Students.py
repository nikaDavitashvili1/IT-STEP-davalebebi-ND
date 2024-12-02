
# შევქმნათ სტუდენტის კლასი აუცილებელი ატრიბუტებით
class Students:
    def __init__(self, name, roll_number, grade):
        self._name = name
        self._roll_number = roll_number
        self.grade = grade

    # მივანიჭოთ კლასის ატრიბუტებს დეკორატორები
    @property
    def name(self) -> str:
        return self._name

    @property
    def roll_number(self) -> int:
        return self._roll_number

    @property
    def grade(self) -> str:
        return self._grade

    @grade.setter
    def grade(self, new_grade: str):
        if new_grade not in ['A', 'B', 'C', 'D', 'E', 'F']:
            raise ValueError("შეფასება უნდა იყოს A, B, C, D, E ან F")
        self._grade = new_grade

    def __str__(self) -> str:
        return f'სახელი: "{self._name}", სიის ნომერი: "{self._roll_number}", შეფასება: "{self._grade}"'

# შევქმნათ სტუდენტების სამართავი კლასი
class StudentManagementSystem:

    # შევქმნათ ცარიელი მასივი სტუდენტებისთვის
    def __init__(self):
        self.students = []

    # სტუდენტთა დამატების მეთოდი:
    def add_student(self, name: str, roll_number: int, grade: str) -> bool:
        # შევამოწმოთ თუ უკვე არსებობს სტუდენტი ამ ნომრით, თუ არადა განვაგრძოთ
        if any(student.roll_number == roll_number for student in self.students):
            print("სტუდენტი ამ ნომრით უკვე არსებობს!\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return False

        try:
            student = Students(name, roll_number, grade)
            self.students.append(student)
            print('სტუდენტი წარმატებით დაემატა!')
            return True
        except ValueError as e:
            print(f'შეცდომა: {e}\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            return False

    # შევქმნათ ყველა სტუდენტის ნახვის მეთოდი
    def view_all_students(self):
        if not self.students:
            print("სტუდენტების სია ცარიელია!\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            return

        print("\nყველა სტუდენტი:")
        i = 1
        for student in self.students:
            print(f'{i}. {student}')
            i += 1

    # შევქმნათ სტუდენტის მოძებნის მეთოდი:
    def search_student(self, roll_number: int) -> Students or None:
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    # შევქმნათ ქულის შეცვლის მეთოდი
    def update_grade(self, roll_number: int, new_grade: str) -> bool:
        student = self.search_student(roll_number)
        if not student:
            print('სტუდენტი ვერ მოიძებნა!\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            return False

        try:
            student.grade = new_grade
            print('შეფასება წარმატებით განახლდა!')
            return True
        except ValueError as e:
            print(f'შეცდომა: {e}\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            return False

# მომხმარებლის მიერ შემოყვანილი მონაცემების ვალიდურობის შემმოწმებლები:
# სახელი:
def validate_student_name(name: str) -> str:
    if not name.strip():
        raise ValueError('სტუდენტის სახელი და გვარი არ უნდა იყოს ცარიელი.\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    if len(name) < 5:
        raise ValueError('სტუდენტის სახელი და გვარი უნდა შეიცავდეს მინიმუმ 5 სიმბოლოს.\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    if not all(char.isalpha() or char.isspace() or char in "-'" for char in name):
        raise ValueError('სტუდენტის სახელი და გვარი უნდა შეიცავდეს მხოლოდ ასოებს, სფეისს, ტირეს ან აპოსტროფს.\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    return name.strip()


# სიის ნომერი:
def validate_roll_number(roll_number_str: str) -> int:
    try:
        roll_number = int(roll_number_str)
        if roll_number <= 0:
            raise ValueError
        return roll_number
    except ValueError:
        raise ValueError('სიის ნომერი დადებითი რიცხვი უნდა იყოს.\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

# ქულა:
def validate_grade(grade: str) -> str:
    grade = grade.upper()
    if grade not in ['A', 'B', 'C', 'D', 'E', 'F']:
        raise ValueError('შეფასება უნდა იყოს A, B, C, D, E ან F.\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    return grade


def main():
    sms = StudentManagementSystem()
    while True:
        print('\n----- სტუდენტების მართვის სისტემა -----')
        print('1. ახალი სტუდენტის დამატება;')
        print('2. ყველა სტუდენტის ნახვა;')
        print('3. სტუდენტის ძებნა ნომრის მიხედვით;')
        print('4. სტუდენტის შეფასების განახლება;')
        print('5. გასვლა.')

        choice = input('\nაირჩიეთ ოპერაცია (1-5): ')

        if choice == '1':
            try:
                name = validate_student_name(input('შეიყვანეთ სტუდენტის სახელი და გვარი: '))
                roll_number = validate_roll_number(input('შეიყვანეთ სიის ნომერი: '))
                grade = validate_grade(input('შეიყვანეთ შეფასება (A, B, C, D, E, F): '))
                sms.add_student(name, roll_number, grade)
            except ValueError as e:
                print(f'შეცდომა: {e}\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

        elif choice == '2':
            sms.view_all_students()

        elif choice == '3':
            try:
                roll_number = validate_roll_number(input('შეიყვანეთ სტუდენტის სიის ნომერი:'))
                student = sms.search_student(roll_number)
                if student:
                    print(f'\nსტუდენტი სიის ნომრით {roll_number}:')
                    print(student)
                else:
                    print(f'სტუდენტი სიის ნომრით {roll_number} ვერ მოიძებნა!')
            except ValueError as e:
                print(f'შეცდომა: {e}\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')


        elif choice == "4":
            try:
                roll_number = validate_roll_number(input("შეიყვანეთ სტუდენტის სიის ნომერი: "))
                new_grade = validate_grade(input("შეიყვანეთ ახალი შეფასება (A, B, C, D, E ან F): "))
                sms.update_grade(roll_number, new_grade)
            except ValueError as e:
                print(f"შეცდომა: {e}\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        elif choice == "5":
            print('მადლობა აპლიკაციის გამოყენებისთვის!')
            break

        else:
            print('\nარასწორი არჩევანი! გთხოვთ სცადოთ თავიდან.')
            print('მინიშნება: ჩაწერეთ რიცხვი 1-დან 5-მდე.')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

if __name__ == '__main__':
    main()
# davaleba 1
print("This is First Task")
def positive_check(func):
    def wrapper(number):
        if number < 0:
            raise ValueError("The number must be positive.")
        else:
            result = func(number)
            print(f"Result: {result}")
            return result
    return wrapper

@positive_check
def return_number(number):
    return number

a = -98
try:
    return_number(-a)
    return_number(a)
except ValueError as e:
    print(e)

# davaleba 2
print("\nThis is Second Task")
class PositiveCheckFunctor:
    def __call__(self, number):
        if number < 0:
            raise ValueError("The number must be positive.")
        else:
            print(f"Result: {number}")
            return number

return_number = PositiveCheckFunctor()

return_number(-a)

# davaleba 3
print("\nThis is Third Task")
import time

def time_calculator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@time_calculator
def example_function():
    # Sample operation
    time.sleep(1)
    return "Completed"

print(example_function())

# davaleba 4
print(f'This is Fourth Task')
class LoggingMeta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Creating class: {name}")
        methods = [attr for attr, val in class_dict.items() if callable(val)]
        print(f"Methods: {methods}")
        return super().__new__(cls, name, bases, class_dict)

class LetsCheckItOut(metaclass=LoggingMeta):
    def method_one(self):
        pass

    def method_two(self):
        pass

    def method_three(self):
        pass

    def method_four(self):
        pass

displayMethods = LetsCheckItOut()
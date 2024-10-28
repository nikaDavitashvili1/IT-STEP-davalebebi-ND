# davaleba 1

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(is_anagram(input("chawere rac ginda: "), input("da getyvi anagramia tu ara: ")))

# davaleba 2

def asos_raodenoba(string, aso):
    return string.count(aso)

print(asos_raodenoba(input("chawere rac ginda: "), "m"))
print(asos_raodenoba(input("chawere rac ginda: "), "a"))
print(asos_raodenoba(input("chawere rac ginda: "), "i"))

# davaleba 3

def fibonacci_sequence(n):
    if n == 1:
        return [0]
    a, b = 0, 1
    sequence = [a]
    for i in range(1, n):
        sequence.append(b)
        a, b = b, a + b
    return sequence

fib_n = int(input("chawere n-is mnishvneloba: "))
print(fibonacci_sequence(fib_n))

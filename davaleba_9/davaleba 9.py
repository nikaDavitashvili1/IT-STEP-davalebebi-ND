# davaleba 1

int_list = [10, 20, 30, 40]

def chavamatot_ricxvi(parametri):
    int_list.append(parametri)
    return int_list
while True:
    try:
        ricxvi = int(input("chawere ricxvi risi chamatebac ginda: "))
        break
    except ValueError:
        print("ricxvi unda chawero")
print("axali sia: \n",chavamatot_ricxvi(parametri=ricxvi))

# davaleba 2

def cifrta_jami(number):
    if number == 0:
        return 0
    else:
        return number % 10 + cifrta_jami(number // 10)

print("cifrta jamia: ", cifrta_jami(123456))

# davaleba 3

def shebrunebuli_striqoni(striqoni):
    if len(striqoni) == 0:
        return ""
    else:
        return striqoni[-1] + shebrunebuli_striqoni(striqoni[:-1])

print("esec shebrunebuli striqoni: ", shebrunebuli_striqoni("): elavwev inedmar xav"))

# davaleba 4

def fibonacis_mimdevroba(n, sequence=None):
    # Initialize the sequence list on the first call
    if sequence is None:
        sequence = []
    if len(sequence) == n:
        return sequence
    if len(sequence) == 0:
        sequence.append(0)
    elif len(sequence) == 1:
        sequence.append(1)
    else:
        sequence.append(sequence[-1] + sequence[-2])
    return fibonacis_mimdevroba(n, sequence)

n = 10
print("fibonacis mimdebroba n=10-stvis: ", fibonacis_mimdevroba(n))

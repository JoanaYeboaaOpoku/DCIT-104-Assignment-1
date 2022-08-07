# Joana Opoku
# ID: 10947185
primeNum = []

number=int(input("Enter Number: "))
def isPrime(y):
    i = 2
    while (i < y):
        if y % i == 0:
            return False
        i = i + 1
    return True


def printNum(x):
    k = 2
    while k <= x:
        if isPrime(k):
            primeNum.append(k)
        k = k + 1


printNum(number)

numOfPrime = len(primeNum)
sum = 0

j = 0
while j < numOfPrime:
    sum += primeNum[j]
    j = j + 1

print(sum)
print("end")

#10 001st Prime

def primeChecker(n):
    if n == 1:
        return False
    if n == 2 :
        return True
    c = 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            c += 1
    if c == 0:
        return True
    return False

      
count = 1
num = 1
while count < 10001:
    num += 2
    if primeChecker(num):
        count += 1
    

print(num)



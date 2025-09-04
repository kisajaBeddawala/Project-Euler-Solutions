#Summation of Primes
import math

def isPrime(n):
    count = 0
    for j in range(2,int(math.sqrt(n))+1):  #use square root of number to reduce time 
        if n % j == 0:
            count += 1
            break
    if count == 0:  #if count is equal to zero it mean there is no other factor instead of 1 and itself
        return True
    return False

total = 2
for i in range(3,2000000,2):
    if isPrime(i):
        total += i

print(total)
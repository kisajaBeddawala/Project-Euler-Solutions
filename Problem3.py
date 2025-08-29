#Largest Prime Factor

#import math library
import math

def isPrime(n):
    count = 0
    for j in range(2,int(math.sqrt(n))+1):  #use square root of number to reduce time 
        if n % j == 0:
            count += 1
    if count == 0:  #if count is equal to zero it mean there is no other factor instead of 1 and itself
        return True
    return False

factor = 1
number = 600851475143
for i in range(3,number,2):
    if number % i == 0 and isPrime(i):
        factor = i

        print(factor)


#this take too much time execute you can choose answer 6857 because there is not other answer print
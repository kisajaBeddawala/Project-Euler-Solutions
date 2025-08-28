#Even Fibonacci Numbers - iterative and recursive methods

#iterative method
n1 = 1
n2 = 2
total = n1 + n2
sum = 2

while total <= 4000000:
    if total % 2 == 0:
        sum += total
    n1 = n2
    n2 = total

    total = n1 + n2

print(sum)

#recursive method
def fib(x,y,s):
    tot = x + y
    if tot > 4000000:
        print(s)
        return
    if tot % 2 == 0:
        s += tot
    fib(y,tot,s)

s = 2
fib(1,2,s)


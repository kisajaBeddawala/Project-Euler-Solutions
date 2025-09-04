#Special Pythagorean Triplet

#a = m^2 - n^2
#b = 2mn
#c = m^2 + n^2

#a + b + c = 1000
#a + b + c = 2m^2 + 2mn
# 0 < n < m

def findTriplet():
    for i in range(1,34):
        for j in range(i+1,35):
            if 2*j**2 + 2*j*i == 1000:
                return [i,j]

ans = findTriplet()
n = ans[0]
m = ans[1]

a = m**2 - n**2
b = 2*m*n
c = m**2 + n**2

print(a*b*c)
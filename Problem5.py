#Smallest Multiple

num = 20

#use while loop because we don't know the upper limit
while True:
    count = 0
    for i in range(1,21):
        if num % i == 0:
            count += 1
    
    if count == 20:
        print(num)
        break

    num += 20       #increase by 20 because the number must be a multiple of 20
#Largest Palindrome Product

def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def answer():
    ans = []
    for i in range(999,99,-1):
        if i % 10 != 0:
            for j in range(999,99,-1):
                if j % 10 != 0 and isPalindrome(i*j):
                    ans.append(i*j)
    
    return max(ans)
                
print(answer())
                

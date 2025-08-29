#Largest Palindrome Product

#function for checking number is palindrome or not
def isPalindrome(num):
    if str(num) == str(num)[::-1]:   #convert number to string and use slicing to check palindrome or not
        return True
    else:
        return False

def answer():
    ans = []        #store all palindrome number because we can't predict first one is always max 
    for i in range(999,99,-1):
        if i % 10 != 0:     #if some number has 0 or 00 as their last digit it can't palindrome 
            for j in range(999,99,-1):
                if j % 10 != 0 and isPalindrome(i*j):
                    ans.append(i*j)
    
    return max(ans)     #return max number from list
                
print(answer())
                

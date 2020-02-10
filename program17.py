#Write a program to find frequency of each digit in a given integer.
def frequencyDigits(n,d): 
    c = 0 
    while (n > 0):  
        if (n % 10 == d): 
            c += 1
        n = n // 10 
    return c 
n=int(input("Enter number: ")) 
d=int(input("Enter a digit: ")) 
print(frequencyDigits(n,d))
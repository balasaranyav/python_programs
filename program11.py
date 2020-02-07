# Write a program to find first and last digit of a number.
def firstDigit(n) : 
    while n >= 10:  
        n = n // 10
    print("First digit is :",end=" ")
    return int(n)

def lastDigit(n) : 
    print("and Last digit is :",end=" ")
    return (n % 10) 
  
n = int(input("Enter a number : "))
print(firstDigit(n), end = " ")  
print(lastDigit(n))
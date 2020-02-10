#Write a program to calculate sum of digits of a number.
def sum(n): 
    value = 0
    while (n > 0): 
        value = value + (n % 10) 
        n = n // 10
    return value 
n = int(input("Enter value: "))
print(sum(n)) 


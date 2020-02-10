#Write a program to calculate product of digits of a number.
 
def product(n): 
    value = 1
    while (n != 0): 
        value = value * (n % 10) 
        n = n // 10
    return value 
n = int(input("Enter value: "))
print(product(n)) 

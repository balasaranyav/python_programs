# Write a program to find HCF (GCD) of two numbers.
def hcf(n, m):
    if n > m:
        smaller = m
    else:
        smaller = n
    for i in range(1, smaller+1):
        if((n % i == 0) and (m % i == 0)):
            hcf = i 
    return hcf
n1=int(input("Enter number1 : "))
n2=int(input("Enter number2 : "))
print("The H.C.F. is",hcf(n1, n2))
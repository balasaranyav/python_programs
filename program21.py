# Write a program to find all factors of a number.
def factor(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
n= int(input("Enter a number : "))
print("The factors for",n, "are : ")
factor(n)

# Write a program to find sum of first and last digit of a number.
def sum():
    n = int(input("Enter a Number :"))
    rev = 0
    first = 0
    sum = 0
    last = n % 10
    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = int(n / 10)
    first = rev % 10
    sum = first + last
    print("Sum of first and last digit is :", sum)
sum()
#Write a program to find sum of all natural numbers between 1 to n.
def natural():
    n = int(input("Enter the value of n: "))
    t = n
    sum = 0
    while n > 0:
        sum = sum + n
        n = n - 1
    print("Sum of first",t, "natural numbers is: ", sum)
natural()
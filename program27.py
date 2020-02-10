# Write a program to find sum of all prime numbers between 1 to n.

def prime(n):
    sum = 0
    for m in range(2, n + 1):
        i = 2
        for i in range(2, m):
            if (int(m % i) == 0):
                i = m
                break
        if i is not m:
            sum += m
    print("\nSum of all prime numbers upto", n, ":", sum)
n=int(input("Enter n value : "))
prime(n)

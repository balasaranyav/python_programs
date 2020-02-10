# Write a program to find all prime factors of a number.

def factor(n):
    for i in range(2, n + 1):
        if(n % i == 0):
            prime = 1
            for j in range(2, (i //2 + 1)):
                if(i % j == 0):
                    prime = 0
                    break
            
            if (prime == 1):
                print(i,"is a Prime Factor of a Given Number" ,n)
n = int(input("Enter Number: "))
factor(n)
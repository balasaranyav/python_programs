# Write a program to check whether a number is Prime number or not  
def prime(n):
    if n > 1: 
        for i in range(2, n//2): 
            if (n % i) == 0: 
                print(n, "is not a prime number") 
        else: 
            print(n, "is a prime number") 
  
    else: 
        print(n, "is not a prime number") 
n = int(input("Enter a number  : "))
prime(n)
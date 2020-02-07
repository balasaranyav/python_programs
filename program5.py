#Write a program to print all odd number between 1 to 100.
def odd():
    n = 1
    m=100
    for i in range(n,m): 
        if i % 2 != 0: 
            print(i, end = " ") 
    print("\r")
odd()
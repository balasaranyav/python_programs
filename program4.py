# Write a program to print all even numbers between 1 to 100. - using while loop
def even():
    n=100
    m=1
    while m < n:
        if(m % 2 == 0):
            print(m)
        m = m + 1
    print("\r")
even()
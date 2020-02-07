# Write a program to find sum of all even numbers between 1 to n.
def even():
    n = int(input(" Please Enter the Maximum Value : "))
    m = 0
    for i in range(1, n):
        if(i % 2 == 0):
            print(i)
            m = m + i
    print("The Sum of Even Numbers from 1 to ",n,"is :",m)
even()
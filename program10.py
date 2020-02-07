# Write a program to count number of digits in a number.
def count(): 
    count = 0
    n = int(input("Enter a number: "))
    while (n > 0):
        n = n//10
        count = count + 1
    print ("Total number of digits : ",count)
count()
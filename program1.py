# Write a program to print all natural numbers from 1 to n. - using while loop
def natural():
    n = int(input("Enter a Number: "))
    i = 1
    print("Natural Numbers from 1 to",n,"are:") 
    while ( i <= n):
        print (i, end = '  ')
        i = i + 1
    print("\r")
natural()
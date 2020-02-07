# Write a program to print all natural numbers in reverse (from n to 1). - using while loop
def reverse():
    n = int(input("Please Enter any Number: "))
    i = n
    print("List of Natural Numbers from",n,"to 1 in Reverse Order : ") 
    while ( i >= 1):
        print (i, end = '  ')
        i = i - 1
    print("\r")
reverse()
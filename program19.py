#Write a program to print all ASCII character with their values.
def ascii(n):
    print("The ASCII value of '" + n + "' is", ord(n))
n=str(input("Enter a charcter : "))
ascii(n)
#Write a program to swap first and last digits of a number.
n = input("Enter a number : ")
new_str = str[-1:] + str[1:-1] + str[:1]
print(new_str)
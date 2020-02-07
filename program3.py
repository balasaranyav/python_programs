# Write a program to print all alphabets from a to z. - using while loop
def alphabets():
    print("Alphabets from a - z are : ")
# a = 97 and z = 122
    for alphabet in range(97, 123):
        print(chr(alphabet), end=" ")
    print("\r")
alphabets()
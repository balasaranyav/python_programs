# Write a program to print multiplication table of any number.
def mul():
    n = int(input("Enter n value: "))
    for i in range(1,11):
        m = n * i
        print(n,"X",i,"=",m)
    print("\r")
mul()
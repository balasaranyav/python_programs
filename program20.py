#Write a program to find power of a number using for loop.
n = int(input("Enter the number of which you have to find power: "))
power = int(input("Enter the power: "))

kj = 1
for n in range(power):
    kj = kj*n

print(kj)
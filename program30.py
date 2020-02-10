#  Write a program to print all Armstrong numbers between 1 to n.
def armstrong():
    for num in range(n,m+ 1):
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        if num == sum:
            print(num)
n = int(input("Enter number1: "))
m = int(input("Enter number2: "))
armstrong()
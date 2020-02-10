# Write a program to check whether a number is Armstrong number or not
def armstrong(n):
    sum = 0  
    temp = n
  
    while temp > 0:  
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
  
    if n == sum:  
        print(n,"is an Armstrong number")  
    else:  
        print(n,"is not an Armstrong number") 
n = int(input("Enter a number: "))
armstrong(n)   
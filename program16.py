#Write a program to enter a number and print its reverse.
def reverse(n):
    Reverse = 0    
    while(n > 0):    
        Reverse = (Reverse *10) + (n % 10) 
        n = n //10    
     
    return (Reverse)
n = int (input("Enter value : "))
print(reverse(n))
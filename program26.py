# Write a program to print all Prime numbers between 1 to n.
def prime():

    for j in range(n,m+ 1):  
        if j > 1:  
            for i in range(2,j):  
                if (j % i) == 0:  
                    break  
            else:  
                print(j) 
n = int(input("Enter  number1: "))  
m = int(input("Enter number2: "))  
prime()
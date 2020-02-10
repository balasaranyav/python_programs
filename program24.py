# Write a program to find LCM of two numbers.

def lcm(n, m):  
    if n > m:  
       greater = n  
    else:  
       greater = m  
    while(True):  
       if((greater % n == 0) and (greater % m == 0)):  
           lcm = greater  
           break  
       greater += 1  
    return lcm  
  
  
n1 = int(input("Enter number1: "))  
n2 = int(input("Enter number2: "))  
print("The L.C.M. of", n1,"and", n2,"is", lcm(n1, n2)) 
#Write a program to enter a number and print it in words.

def words (n):
    dictionary = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",'7': "seven", '8': "eight", '9': "nine", '0': "zero"}
    return " ".join(map(lambda x: dictionary[x], str(n)))

n=int(input("Enter number : "))
print(words(n))

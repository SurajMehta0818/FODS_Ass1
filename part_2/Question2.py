'''Write a program that prompts the user for two integer values and displays the results of the first
 number divided by the second, with exactly two decimal places displayed. [5]'''
a = int(input("Enter any number:"))
b = int(input("Enter any number again:"))
result = a/b
print(round(result,2))


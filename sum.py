number1 = int(input("Enter the firstnumber:"))
number2 = int(input("Enter the secondnumber:"))

def sum(num1,num2):
    sum = num1+num2
    return sum 

x = sum(number1,number2)
print("Sum of the given number is {0} ".format(x))
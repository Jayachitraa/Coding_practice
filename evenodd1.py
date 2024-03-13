number = int(input("Enter the Number:"))
if number <= 0:
    print("Enter the vadild number")
elif number % 2 == 0:
    print("The given number is even!!!")
else:
    print("The given number is odd number!!!")

 
def evenodd(number):
    for i in number:
        if i <= 0:
            print("Enter the vadild number")
        elif i % 2 == 0:
            print("The given number is even!!!")
        else:
            print("The given number is odd number")

x = [1,2,3,4,5,6,7,7,8,9,0]
evenodd(x)


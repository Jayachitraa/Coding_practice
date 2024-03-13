# number = int(input("Enter the number:"))

# if number ==0:
#     print("Pls enter the number above zoro!!!")
# elif number>0:
#     print("The given number {0} is positive number".format(number))
# else:
#     print("The given number{0} is negative number".format(number))


def positiveneg(number):
    for i in number:
        if i ==0:
            print("Pls enter the number above zoro!!!")
        elif i>0:
            print("The given number {0} is positive number".format(i))
        else:
            print("The given number{0} is negative number".format(i))

x = [1,2,3,-1,-4,-0,6,]
positiveneg(x)
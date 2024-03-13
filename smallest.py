# def find_smallest(numbers):


#     smallest = numbers[0]

#     for num in numbers:
#         if num < smallest:
#             smallest = num

#     return smallest

 
# my_numbers = [10, 5, 8, 12, 7]
# result = find_smallest(my_numbers)
# print("Smallest number:", result)


def second_largest(num):
    largest_number = num[0]
    for n in num:
        if n > largest_number:
           largest_number = n
           print("largest_number111:",largest_number)
    for n in num:
        if n > largest_number and n!= largest_number:
            largest_number = n
            print("largest_number222:",largest_number)
    return  largest_number
        

my_numbers = [10, 5, 8, 12, 7]
result = second_largest(my_numbers)
print("Smallest number:", result)    
    

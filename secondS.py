def secsmall(numbers):
    small = max(numbers)
    for i in range(len(numbers)):
        if numbers[i]>min(numbers):
            if numbers[i]<small:
                small = numbers[i]
    return small

my_numbers = [10, 5, 8, 12, 7]
result = secsmall(my_numbers)
print("Second smallest number:", result)
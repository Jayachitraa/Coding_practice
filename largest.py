def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

# Example usage:
my_numbers = [10, 5, 8, 12, 7]
result = find_largest(my_numbers)
print("Largest number:", result)

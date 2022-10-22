"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if len(numbers)%2 == 1:
            print(numbers[(len(numbers)-1)/2])
        elif len(numbers)%2==0:
            num1 = numbers[len(numbers)/2]
            num2 = numbers[(len(numbers)/2)-1]
            print((num1+num2)/2)

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

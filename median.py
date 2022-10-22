"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if len(numbers)%2 == 1:
            index = int((len(numbers)-1)/2)
            print(numbers[index])
        elif len(numbers)%2==0:
            index = int(len(numbers)/2)
            num1 = numbers[index]
            num2 = numbers[index-1]
            print((num1+num2)/2)

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

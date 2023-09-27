while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
numbers.sort()
middleNum = len(numbers)//2
median = (numbers[middleNum]+numbers[~middleNum])/2
print(f'median number is {median}')
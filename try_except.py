# 1. Age Converter
# try:    
#     age = input("Enter your age: ")
#     next_year = int(age) + 1
#     print("Next year you will be", next_year)
# except ValueError:
#     print("Age must be a number ")
# 2. Safe Division
# try:
#     a = int(input("First number: "))
#     b = int(input("Second number: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero ")
# 3. Number From List
# numbers = [10, 20, 30]
# try:
#     index = int(input("Choose index: "))
#     print(numbers[index])
# except IndexError:
#     print("Index not found ")
# 4. Dictionary Lookup
# prices = {
#     "apple": 3,
#     "banana": 5}

# try:
#     item = input("Enter item: ")
#     print(prices[item])
# except KeyError:
#     print(" Item not found ")
# 5. Multiple Error Types
numbers = [100, 200, 300]

try:
    index = int(input("Choose index: "))
    divider = int(input("Choose divider: "))

    result = numbers[index] / divider
    print(result) 
except ValueError:
    print("error: invalid number input")
except IndexError:
    print("error: list index out of range")           
except ZeroDivisionError:
    print("error: division by zero")    

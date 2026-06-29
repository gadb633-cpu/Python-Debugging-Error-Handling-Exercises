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
# numbers = [100, 200, 300]

# try:
#     index = int(input("Choose index: "))
#     divider = int(input("Choose divider: "))

#     result = numbers[index] / divider
#     print(result) 
# except ValueError:
#     print("error: invalid number input")
# except IndexError:
#     print("error: list index out of range")           
# except ZeroDivisionError:
#     print("error: division by zero")    
# 6. Finally Message
# try:
#     score = int(input("Enter score: "))
#     print("Your score is", score)
# except ValueError:
#     print("Invalid score ")
# finally:
#     print("Check finished ")    
# 7. Syntax Error vs Runtime Error
# name = input("Enter your name: ")
# if name == "admin":
#     print("Welcome admin")
# else:
#     print("Welcome user")
# the try/except is for error of expected things and not a syntax error
# 8. Wrong Discount
# price = 100
# discount = 20
# print(discount/100) # this the bug
# final_price = (price/100)*(100-discount)
# print(final_price) # 99.8
# # 9. Login Attempts Logic Bug
# password = "abc123"
# guess = input("Enter password: ")

# if guess == password:
#     print("Login successful")
# else:
#     print("Wrong password")
# # logicalerror
# # the bug is at line 72 != 
# 10. Safe Calculator
# try:
#     num1 = int(input("Number 1: "))
#     op = input("Operator: ")
    
#     num2 = int(input("Number 2: "))

#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "/":
#         print(num1 / num2)  
#     else:
#         print("Unknown operator")    
# except ZeroDivisionError:
#     print("error: division by zero")   
# except ValueError:
#     print("error: is not a number")    
# finally:
#     print("Calculator closed")   

# Extra 1. Temperature Converter
# celsius = input("Celsius: ")
# try:
#     fahrenheit = int(celsius) * 9 / 5 + 32
#     print(fahrenheit)      
# except ValueError:
#     print("error: Temperature must be a number ")

# Extra 2. First Letter
# try:
#     word = input("Enter word: ")
#     print(word[0])    
# except IndexError:
#     print("error: Word is empty")    

# # Extra 3. Average Score
# scores = [90, 80, 100]
# total = 0

# for score in scores:
#     total += score

# average = total / len(scores)
# print(average) # 33.336
# # expected average is: 90

# # Extra 4. Product Price
# products = {
#     "pen": 4,
#     "notebook": 12}

# try:
#     product = input("Product: ")
#     amount = int(input("Amount: "))

#     print(products[product] * amount)
# except KeyError:
#     print("error: the key is not exsict ")
# except ValueError:
#     print("error: the price is only a number ")

# # Extra 5. File Name Check Without File Handling
# files = ["data.txt", "users.csv", "notes.txt"]

# try:
#     choice = int(input("Choose file number: "))
#     print(files[choice])
# except ValueError:
#     print("error: enter only number ")
# except IndexError:
#     print("error: the index out of range")

# Extra 6. Wrong Maximum
numbers = [4, 10, 2, 8]
maximum = 0

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
# the wrong output is all the time the number is biger
# the expected output is 10
# logicalerror

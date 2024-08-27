# The Greatest Showdown
#Task 1: Identify the Greatest. Write a Python program that 
# asks the user to enter three numbers. Your code should then 
# identify and print out the largest number among the three...


num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number:"))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is:{largest}")
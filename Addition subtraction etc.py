#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      abc
#
# Created:     31/03/2023
# Copyright:   (c) abc 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
first = input("Enter the first number")
second = input("enter the second number")
i=2
sum = int(first) + int(second)
print("the sum is:" , sum)
Multiply = int(first) * int(second)
print("The multiplication of the first and second number is:" , Multiply)
Division = int(first) / int(second)
print("The division of the first and second number is:" , Division)
Subtraction = int(first) - int(second)
print("The subtraction of the first and second number is:" , Subtraction)
Remainder = int(first) % int(second)
print("The remainder of the first and second number is" , Remainder)
Power = int(first) ** int(second)
print("The power of the first number to the second number is", Power)
#("Addition- + ,Subtraction - - , Multiplication - *, Division - / , Power - **, Remainder- %")
#while is a keyword is python #no infinite loop in our course
#while i <=10
while i <=10:
    print(i *"*")
    i = i+1




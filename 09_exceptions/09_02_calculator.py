'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


try:
    x = int(input("Please write your first number :"))
    y = int(input("Please write your second number :"))
    division = x/y
except ZeroDivisionError:
    print("You can't divide by zero !")
except ValueError:
    print("You have to enter a number !")


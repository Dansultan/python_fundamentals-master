'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

first = input("Please write your first sentence : ")
second = input("Please write your second setence : ")
third = input("Please write your third sentence : ")

print(len(first),",",first)
print(len(second),",",second)
print(len(third),",",third)

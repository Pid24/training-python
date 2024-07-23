#Data Types

#String
print("HELLO"[4])
print("123" + "456")

#Integer
print(123 + 456)

#Float
3.14159

#Boolean
True
False

#Convert string to integer
num_char = len(input("What is your name "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

#Convert integer to string and integer to float
a = str(123)
print(type(a))
b = float(123)
print(type(b))

#Math operation
3 + 5
7 - 4
3 * 2
2 ** 3

# PEMDASLR
# ()
# **
# *
# * /
# + -
print(3 * (3 + 3) / 3 - 3)

#Number manipulation
print(type(8 // 3))
result = 4 / 2

score = 0
height = 1.8
isWinning = True
#F-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#Quiz
print(6 + 4 / 2 - (1 * 2))
a = int("5") / int(2.7)
name = input("What is your name?")
print(f"Hello, {name}")
name = input("What is your name?")
print("Hello, " + name)
age = 12
print(f"Your are {age} years old")
age = 12
print("Your are " +  age + " years old")
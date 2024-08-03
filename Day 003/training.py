# Control flow with If/Else
water_level = 150
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Nested If/Else and Elif
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $7.")
    elif age <= 18:
        print("Please pay $14.")
    else:
        print("Please pay $21.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Multiple If statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 7
        print("Child tickets are $7.")
    elif age <= 18:
        bill = 14
        print("Youth tickets are $14.")
    else:
        bill = 21
        print("Adult tickets are $21.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

#Logical Operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 7
        print("Child tickets are $7.")
    elif age <= 18:
        bill = 14
        print("Youth tickets are $14.")
    elif age >= 35 and age <= 70:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 21
        print("Adult tickets are $21.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

#Quiz
# not 5 = 5
False or True or False
a = 5
b = 7
 
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")
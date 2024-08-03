#Random Module
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

print(my_module.pi)

#Understanding the offset and appending Items to Lists
states_of_america = ["Delaware", "Ohio", "Alaska", "Arizona", "Arkansas"]

states_of_america[1] = "Ohio"

states_of_america.extend(["Annafie", "Rofid"])

# states_of_america.append("Annafie")

print(states_of_america)

#IndexErrors
states_of_america = ["Delaware", "Ohio", "Alaska", "Arizona", "Arkansas"]

print(states_of_america)

dirty_dozen = ["Strawberry", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberry", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetable = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetable]
print(dirty_dozen)
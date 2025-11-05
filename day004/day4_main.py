import random
import my_module
from Day003.day3_love_calculator import love_score

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)

#How to create random floating point number between 0 and 5
random_float = random.random() * 5 #The multiplication by 5 allows changing range from 0.0000 - 0.99999 to times 5

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

# import random
# import my_module
import random

# ran_int = random.randint(a=1, b=10)
# print(ran_int)

# print(my_module.my_fav_num)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)
#
# random_float = random.uniform(1, 10)
# print(random_float)

random_number = random.randint(a=1, b=10)

print(random_number)

if random_number % 2  == 0:
    print("Heads")
else:
    print("Tails")
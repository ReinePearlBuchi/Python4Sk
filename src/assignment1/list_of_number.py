import random
def generate_ten_number_in_list():
    ten_list = [random.randint(1, 10) for i in range(10)]
    return ten_list

print(generate_ten_number_in_list())

#  use dot seed when you dont want your random number to change
# list = range(1,50,10)
# for i in list:
#     print(i)
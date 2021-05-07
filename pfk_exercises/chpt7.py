from chpt7_functions import name_picker, room_picker

#list_of_stuff = ['pair of socks', 'hat', 'banana']

# list_of_stuff = ['7', '10', '39', '40']
# random_item = np.random.choice(list_of_stuff)

# random_age = np.random.randint(9, 11)

# print("Are you " + str(random_age) + " years old?")

result1 = name_picker()
result2 = room_picker()

print(result1 + " in the " + result2)
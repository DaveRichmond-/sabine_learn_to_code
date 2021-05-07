import numpy as np

# def sff(name):
#   print("Hello.  I'm " + name + "'s first function.")

# def sof(S, D):
#   T = S / D
#   return T

# list_of_stuff = ['pair of socks', 'hat', 'banana']
# random_item = np.random.choice(list_of_stuff)

def name_picker():
  names = ["Daddy", "Mommy", "Sabine", "Nella", "Svea", "Boo", "Pebbles", "Oyla", "Haty"]
  chosen_name = np.random.choice(names)
  return chosen_name

def room_picker():
  rooms = ["Front Bathroom", "Dining Room", "Kitchen", "Living Room", "Office", "S & N Room", "M & D", "Back Bathroom"]
  HideSeek = np.random.choice(rooms)
  return HideSeek

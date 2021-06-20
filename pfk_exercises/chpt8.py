from chpt8_classes import Giraffes

geoffrey = Giraffes(number_spots=101, name='Geoffery')

# print(geoffrey.name)

# geoffrey.breathe()
# geoffrey.eat_leaves_from_tall_trees(num_leaves=100)

print(f"Ahh, life is good. I have {geoffrey.number_spots} spots.")
print("")
print("Something weird is happening. I'm in the middle of a spot tornado!")
while geoffrey.number_spots < 999:
  geoffrey.add_spot()
print("")
print(f"Oh no!  I have {geoffrey.number_spots} spots!!!")

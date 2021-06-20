class Animals():
  def breathe(self):
    print("FINALLY! I can breathe again. Sabine, next time can you immediately press 'Breathe'?")
  def move(self):
    print("Hmmm, I wonder what's over here.")
  def eat_food(self):
    print("Numnumnum, that's some yummy food.")

class Mammals(Animals):
  def feed_young_with_milk(self):
    print("Here's some yummy milk for you.")

class Giraffes(Mammals):
  def __init__(self, number_spots, name):
    self.number_spots = number_spots
    self.name = name
  def eat_leaves_from_tall_trees(self, num_leaves):
    print(f"I'm so glad I can reach these {num_leaves} yummy leaves way up here.")
  def remove_spot(self):
    self.number_spots = self.number_spots - 1
  def add_spot(self):
    self.number_spots = self.number_spots + 1



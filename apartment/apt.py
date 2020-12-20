class apartment:
  def __init__(self, name, rooms):
    self.name = name
    self.rooms = rooms

  def sq_ft(self):
    sq_ft = 0
    for room in self.rooms:
      sq_ft += self.rooms[room][0] * self.rooms[room][0]
    return sq_ft

  def largest_rm(self):
    largest_area = 0
    for room in self.rooms:
      area = self.rooms[room][0] * self.rooms[room][0]
      if area > largest_area:
        largest_area = area
        largest_room = room
    return largest_room, largest_area


def main():
  # frederick25 measurements
  fred25 = apartment("frederick_25",
    {
    'entrance': (3,3),
    'frontbath': (4,4),
    'dining': (2,2),
    'kitchen': (1,1),
    'living': (5,5),
    'hall': (1,4),
    'office': (4,3),
    'girlsroom': (10,10),
    'DGroom': (9,9),
    'backbath': (3,4)
    })

  print("The size of " + fred25.name + " is: " + str(fred25.sq_ft()))

  largest_room, largest_area = fred25.largest_rm()
  print("The largest room in " + fred25.name + " is the " + largest_room)
  print("The " + largest_room + " is " + str(largest_area) + " sq. ft.")    

  return


if __name__ == '__main__':
  main()
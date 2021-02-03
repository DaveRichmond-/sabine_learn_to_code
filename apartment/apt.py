class apartment:
  def __init__(self, name, rooms):
    self.name = name
    self.rooms = rooms

  def sq_ft(self):
    sq_ft = 0
    for room in self.rooms:
      sq_ft += self.rooms[room][0] * self.rooms[room][1]
    return sq_ft

  def largest_rm(self):
    largest_area = 0
    for room in self.rooms:
      area = self.rooms[room][0] * self.rooms[room][1]
      if area > largest_area:
        largest_area = area
        largest_room = room
    return largest_room, largest_area


def main():
  # frederick25 measurements
  fred25 = apartment("frederick_25",
    {
    'entrance': (9,8),
    'front bath': (5,8),
    'dining room': (9,12),
    'kitchen': (9,12),
    'living room': (19,12),
    'hall_1': (4,7),
    'hall_2': (3,3),
    'back closet': (4,6),
    'office': (13,12),
    'girls room': (13,12),
    'DG room': (10,12),
    'back bath': (7,8)
    })

  print("The size of " + fred25.name + " is: " + str(fred25.sq_ft()) + " sq. ft.")

  largest_room, largest_area = fred25.largest_rm()
  print("The largest room in " + fred25.name + " is the " + largest_room)
  print("The " + largest_room + " is " + str(largest_area) + " sq. ft.")    

  return


if __name__ == '__main__':
  main()
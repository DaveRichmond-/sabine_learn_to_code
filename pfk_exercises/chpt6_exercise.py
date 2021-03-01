import turtle

s = turtle.Pen()



# for b in range(50):
#   for a in range(4):
#     s.forward(length)
#     s.left(90)
#   length = length + 2

# s.forward(5)
# s.left()


# length = 0.5
# for a in range(360):
#   s.forward(length)
#   s.left(1)
#   length = +2

# worlds easiest maze (a.k.a spiral)-0&----0
length = 0.1
num_loops = 10
for a in range(num_loops * 360):
  s.forward(length)
  s.left(1)
  length = length + 0.001

# ear shape----0
# num_loops = 1
# s.left(90)
# for a in range(num_loops * 360):
#   if a < 90 or a > 270:
#     length = 0.2
#   if a > 90 and a < 270:
#     length = 0.5
#   s.forward(length)
#   s.left(1)

# Snail-0
# Shell
# length = 0.1
# num_loops = 5
# for a in range(num_loops * 360):
#   s.forward(length)
#   s.left(1)
#   length = length +0.001
# # Neck
# length = 0.1
# s.forward(length)
# s.left(2)
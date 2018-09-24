import math

class Point: # define cartesian points
	def __init__(self, x, y):
		self.x = x # x - coordinate
		self.y = y # y - coordinate

def distance(A, B):
	# distance b/w two cartesian points
	# d = sqrt( (x2-x1)^2 + (y2-y1)^2 )
	return math.sqrt((B.x - A.x) * (B.x - A.x) + (B.y - A.y) * (B.y - A.y))
	
def isRectangle(a, b, c, d):
	# Calculating diagonals
	ac = distance(a, c)
	bd = distance(b, d)

	if ac == bd: # diagonals are equal only for rectangles
		return True

	return False

# Main
a = Point(-1, -1)
b = Point(-1, 1)
c = Point(1, 1)
d = Point(1, -1)

print(isRectangle(a, b, c, d))
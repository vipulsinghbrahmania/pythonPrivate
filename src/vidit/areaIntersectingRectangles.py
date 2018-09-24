class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def intersectingArea(l1, r1, l2, r2):
	return abs(min(r1.x, r2.x) - max(l1.x, l2.x)) * abs(min(r1.y, r2.y) - max(l1.y, l2.y)) 

left1 = Point(2, 2)
right1 = Point(5, 7)

left2 = Point(3, 4)
right2 = Point(6, 9)

print(intersectingArea(left1, right1, left2, right2))
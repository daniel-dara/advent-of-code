# Ordered list of directions useful for calculating turns.
DIRECTIONS = '^>v<'

class Cart:
	def __init__(self, row, col, orientation, turn):
		self.row = row
		self.col = col
		self.orientation = orientation
		self.turn = turn

	def turnLeft(self):
		self.orientation = DIRECTIONS[(DIRECTIONS.index(self.orientation) - 1) % len(DIRECTIONS)]

	def turnRight(self):
		self.orientation = DIRECTIONS[(DIRECTIONS.index(self.orientation) + 1) % len(DIRECTIONS)]

	def move(self):
		# Move to the next location.
		self.row += int(self.orientation == 'v') - int(self.orientation == '^')
		self.col += int(self.orientation == '>') - int(self.orientation == '<')

		# Retrieve the new track piece.
		track = grid[self.row][self.col]

		# Correct orientation for curves and intersections.
		if track == '\\' and self.orientation in '<>' or track == '/' and self.orientation in '^v':
			self.turnRight()
		elif track == '\\' and self.orientation in '^v' or track == '/' and self.orientation in '<>':
			self.turnLeft()
		elif track == '+':
			if self.turn == 0:
				self.turnLeft()
			elif self.turn == 2:
				self.turnRight()

			self.turn = (self.turn + 1) % 3

	def collidesWith(self, cart):
		return self != cart and self.row == cart.row and self.col == cart.col

# Parse input.
grid = [list(line.rstrip('\n')) for line in open('input.txt')]

# Find the carts.
carts = []
for row in range(len(grid)):
	for col in range(len(grid[0])):
		if grid[row][col] in 'v^<>':
			# Store the carts with their orientation and a counter indicating their next turn decision.
			carts.append(Cart(row, col, grid[row][col], 0))

			# Remove carts from the grid so they don't mess up traversal code.
			grid[row][col] = '-' if grid[row][col] in '<>' else '|'


def find_collision():
	while True:
		for cart in carts:
			cart.move()

			if True in list(map(cart.collidesWith, carts)):
				return cart.col, cart.row


print(find_collision())

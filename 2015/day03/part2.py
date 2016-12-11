visits = set([(0, 0)])
locs = [(0, 0), (0, 0)]

def move(loc, c):
	return (loc[0] + int(c == '>') - int(c == '<'), loc[1] + int(c == '^') - int(c == 'v'))

for line in open('input.txt'):
	for i in range(len(line)):
		locs[i % 2] = move(locs[i % 2], line[i])
		visits.add(locs[i % 2])
		
print(len(visits))
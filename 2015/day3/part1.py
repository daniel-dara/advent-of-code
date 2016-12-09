visits = set([(0, 0)])
loc = (0, 0)

for line in open('input.txt'):
	for c in line:
		loc = (loc[0] + int(c == '>') - int(c == '<'), loc[1] + int(c == '^') - int(c == 'v'))
		visits.add(loc)

print(len(visits))
import copy

# {elevator}-[0M,0G,1M],[1G],[],[]
def getHash(floors, elevator):
	return str(elevator) + str([(len(floors[i]), sum(x[1] == 'G' for x in floors[i])) for i in range(4)])

def move(direction, elevator, item, floors, index = -1):
	floors[elevator].remove(item)
	index = index if index != -1 else len(floors[elevator + direction])
	floors[elevator + direction].insert(index, item)

# State is valid if the elevator floor is non-empty and floors with generators do not have any unpaired chips.
def isValidState(floors, elevator, allow_empty = False):
	if not floors[elevator] and not allow_empty:
		return False

	hasGen = False
	unpaired = False

	for item in floors[elevator]:
		if item[1] == 'M':
			unpaired |= (item[0] + 'G') not in floors[elevator]
		else:
			hasGen = True

	return not (hasGen and unpaired)

def explore(queue):
	while queue:
		node = queue.pop(0)
		elevator, floors, moves, last_state = node
		val = getHash(floors, elevator)

		# Return if we've already reached this state.
		if val in states:
			continue

		# Set the move count for the current state.
		states[val] = {'moves': moves, 'last': last_state}

		if elevator == 3 and val == getHash(end, 3):
			print("FOUND SOLUTION", moves)
			return

		# Explore new states, move up/down with 1/2 items.
		for index1 in range(len(floors[elevator])):
			item = floors[elevator][index1]

			for index2 in range(index1 + 1, len(floors[elevator])):
				item2 = floors[elevator][index2]

				if item == item2:
					continue

				if elevator < 3:
					move(1, elevator, item, floors)
					move(1, elevator, item2, floors)

					if getHash(floors, elevator + 1) not in states and isValidState(floors, elevator + 1) and isValidState(floors, elevator, True):
						queue.append([elevator + 1, copy.deepcopy(floors), moves + 1, val])

					move(-1, elevator + 1, item, floors, index1)
					move(-1, elevator + 1, item2, floors, index2)

				if elevator > 0:
					move(-1, elevator, item, floors)
					move(-1, elevator, item2, floors)

					if getHash(floors, elevator - 1) not in states and isValidState(floors, elevator - 1) and isValidState(floors, elevator, True):
						queue.append([elevator - 1, copy.deepcopy(floors), moves + 1, val])

					move(1, elevator - 1, item, floors, index1)
					move(1, elevator - 1, item2, floors, index2)

			if elevator < 3:
				move(1, elevator, item, floors)

				if getHash(floors, elevator + 1) not in states and isValidState(floors, elevator + 1) and isValidState(floors, elevator, True):
					queue.append([elevator + 1, copy.deepcopy(floors), moves + 1, val])

				move(-1, elevator + 1, item, floors, index1)

			if elevator > 0:
				move(-1, elevator, item, floors)

				if getHash(floors, elevator - 1) not in states and isValidState(floors, elevator - 1) and isValidState(floors, elevator, True):
					queue.append([elevator - 1, copy.deepcopy(floors), moves + 1, val])

				move(1, elevator - 1, item, floors, index1)

useSample = False

if not useSample:
	# floors = [['PG', 'PM'], ['BG', 'CG', 'RG', 'LG'], ['BM', 'CM', 'RM', 'LM'], []]
	floors = [['PG', 'PM', 'ZG', 'ZM', 'XG', 'XM'], ['BG', 'CG', 'RG', 'LG'], ['BM', 'CM', 'RM', 'LM'], []] # 33 is right answer
	# floors = [['PG', 'PM'], ['BG', 'CG', 'RG'], ['BM', 'CM', 'RM'], []]
	# floors = [['PG', 'PM'], ['BG', 'CG'], ['BM', 'CM'], []]
else:
	floors = [['HM', 'LM'], ['HG'], ['LG'], []] # 11 moves

end = [[], [], [], sum(floors, [])]

elevator = 0;
states = {}
queue = []

# print(getHash())
queue.append([elevator, copy.deepcopy(list(floors)), 0, 'origin'])
explore(queue)

for state in states:
	print(state)

print('total states:', len(states))

floors = end

if getHash(end, 3) not in states:
	print('didn\'t reach final state :(')
else:
	print('DONE, moves: '+ str(states[getHash(end, 3)]))
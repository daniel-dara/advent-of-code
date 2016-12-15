import copy

# {elevator}-[0M,0G,1M],[1G],[],[]
def getHash(elevator, floors):
	return str(elevator) + str([(len(floors[i]), sum(x[1] == 'G' for x in floors[i])) for i in range(4)])

def move(elevator, floors, direction, from_index, to_index):
	floors[elevator + direction].insert(to_index, floors[elevator].pop(from_index))

def exploreState(elevator, floors, direction, moves, cur_hash, index1, index2 = None):
	if index2:
		move(elevator, floors, direction, index2, 0)

	move(elevator, floors, direction, index1, 0)

	next_hash = getHash(elevator + direction, floors)

	if next_hash not in states and isValidState(elevator + direction, floors) and isValidState(elevator, floors, True):
		queue.append([elevator + direction, copy.deepcopy(floors), moves + 1, cur_hash, -direction, next_hash])

	move(elevator + direction, floors, -direction, 0, index1)

	if index2:
		move(elevator + direction, floors, -direction, 0, index2)

# State is valid if the elevator floor is non-empty and floors with generators do not have any unpaired chips.
def isValidState(elevator, floors, allow_empty_floors = False):
	if not allow_empty_floors and not floors[elevator]:
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
		elevator, floors, moves, last_state, last_dir, cur_hash = node

		# Return if we've already reached this state.
		if cur_hash in states:
			continue

		# Set the move count for the current state.
		states[cur_hash] = {'moves': moves, 'last': last_state}

		if elevator == 3 and cur_hash == getHash(3, end):
			print("FOUND SOLUTION:", moves)
			return

		# Explore new states, move up/down with 1/2 items.
		for index1 in range(len(floors[elevator])):

			for index2 in range(index1 + 1, len(floors[elevator])):
				if elevator < 3:
					exploreState(elevator, floors, 1, moves, cur_hash, index1, index2)

				if elevator > 0:
					exploreState(elevator, floors, -1, moves, cur_hash, index1, index2)

			if elevator < 3:
				exploreState(elevator, floors, 1, moves, cur_hash, index1)

			if elevator > 0:
				exploreState(elevator, floors, -1, moves, cur_hash, index1)

useSample = False

if not useSample:
	# floors = [['PG', 'PM'], ['BG', 'CG', 'RG', 'LG'], ['BM', 'CM', 'RM', 'LM'], []]
	floors = [['PG', 'PM', 'ZG', 'ZM', 'XG', 'XM'], ['BG', 'CG', 'RG', 'LG'], ['BM', 'CM', 'RM', 'LM'], []]
else:
	floors = [['HM', 'LM'], ['HG'], ['LG'], []] # 11 moves

end = [[], [], [], sum(floors, [])]

elevator = 0
states = {}
queue = []

queue.append([elevator, copy.deepcopy(list(floors)), 0, 'origin', 0, getHash(elevator, floors)])

explore(queue)

print('total states:', len(states))

floors = end

if getHash(3, end) not in states:
	print('didn\'t reach final state :(')
else:
	print('DONE, moves: '+ str(states[getHash(3, end)]))
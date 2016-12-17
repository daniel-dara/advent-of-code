from hashlib import md5

def unlock(path):
	return [not c.isdigit() and c != 'a' for c in md5(bytes('pxxbnzuo' + path, 'ascii')).hexdigest()[:4]]

def findLongestPath(queue):
	longest_path = ''

	while queue:
		x, y, path = queue.pop(0)

		if (x, y) == (3, 3):
			longest_path = max(longest_path, path, key=len)
		else:
			if x < 0 or y < 0 or x >= 4 or y >= 4:
				continue

			unlocked = unlock(path)

			if unlocked[0]:
				queue.append((x, y - 1, path + 'U'))

			if unlocked[1]:
				queue.append((x, y + 1, path + 'D'))

			if unlocked[2]:
				queue.append((x - 1, y, path + 'L'))

			if unlocked[3]:
				queue.append((x + 1, y, path + 'R'))

	return longest_path

print(len(findLongestPath([(0, 0, '')])))

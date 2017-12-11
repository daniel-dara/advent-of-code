import json

queue = json.loads(open('input.txt').read())
total = 0

while queue:
	obj = queue.pop()

	if isinstance(obj, list):
		queue += obj
	elif isinstance(obj, dict):
		if 'red' not in obj.values():
			queue += obj.values()
	elif isinstance(obj, int):
		total += int(obj)

print(total)
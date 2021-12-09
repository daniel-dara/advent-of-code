
history = {value: i + 1 for i, value in enumerate(map(int, open('input.txt').readline().split(',')))}
previous = list(history)[-1]

for turn in range(len(history), 30_000_000):
	history[previous], previous = turn, turn - history.get(previous, turn)

print(previous)

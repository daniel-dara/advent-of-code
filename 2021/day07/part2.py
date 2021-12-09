
def gauss_sum(n: int) -> int:
	return n * (n + 1) // 2


positions = sorted(map(int, open('input.txt').read().split(',')))

fuel_per_position = (
	sum(gauss_sum(abs(p - i)) for p in positions)
	for i in range(positions[-1])
)

print(min(fuel_per_position))

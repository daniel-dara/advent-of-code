from functools import reduce

# A readable solution
def calculate1(fuel):
	fuel_needed = (fuel // 3) - 2

	if fuel_needed <= 0:
		return []

	return [fuel_needed] + calculate1(fuel_needed)

# A less readable solution using a generator and hard coding the # 2nd-to-last-lowest fuel value.
def calculate2(fuel):
	while fuel >= 8:
		fuel = (fuel // 3) - 2
		yield fuel

# A janky two-liner relying on manipulation of the for-loop variable
def calculate3(fuel):
	for fuel in iter(lambda: max(0, (fuel // 3) - 2), 0):
		yield fuel

print(sum([sum(calculate1(int(mass))) for mass in open('input.txt')]))


def binary_space_partition1(low: int, high: int, low_char: str, sequence: str) -> int:
	for char in sequence:
		half_range = (high - low + 1) // 2

		if char == low_char:
			high -= half_range
		else:
			low += half_range

	return low


def get_seat_id1(boarding_pass: str) -> int:
	row = binary_space_partition1(0, 127, 'F', boarding_pass[:7])
	column = binary_space_partition1(0, 7, 'L', boarding_pass[7:10])
	return row * 8 + column


def binary_space_partition2(high: int, low_char: str, sequence: str) -> int:
	distance = high + 1

	for index, char in enumerate(sequence):
		if char == low_char:
			high -= distance // 2 ** (index + 1)

	return high


def get_seat_id2(boarding_pass: str) -> int:
	row = binary_space_partition2(127, 'F', boarding_pass[:7])
	column = binary_space_partition2(7, 'L', boarding_pass[7:10])
	return row * 8 + column


def get_seat_id3(boarding_pass: str) -> int:
	row = int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)
	column = int(boarding_pass[7:10].replace('L', '0').replace('R', '1'), 2)
	return row * 8 + column


boarding_pass = sorted(open('input.txt').readlines())[0]
print(get_seat_id1(boarding_pass))
print(get_seat_id2(boarding_pass))
print(get_seat_id3(boarding_pass))

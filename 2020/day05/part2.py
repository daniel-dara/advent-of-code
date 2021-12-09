
def get_seat_id(boarding_pass: str) -> int:
	row = int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)
	column = int(boarding_pass[7:10].replace('L', '0').replace('R', '1'), 2)
	return row * 8 + column


ids = sorted(get_seat_id(line) for line in open('input.txt'))
print(next(a + 1 for a, b in zip(ids, ids[1:]) if a + 1 != b))

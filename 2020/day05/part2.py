
def get_seat_id(boarding_pass: str) -> int:
	return int(boarding_pass.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2)


ids = sorted(get_seat_id(line) for line in open('input.txt'))
print(next(a + 1 for a, b in zip(ids, ids[1:]) if a + 1 != b))

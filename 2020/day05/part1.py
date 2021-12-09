
def get_seat_id(boarding_pass: str) -> int:
	return int(boarding_pass.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2)


print(get_seat_id(sorted(open('input.txt').readlines(), key=lambda x: x.replace('L', 'Z'))[0]))

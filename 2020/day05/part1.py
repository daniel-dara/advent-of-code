
def get_seat_id(boarding_pass: str) -> int:
	row = int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)
	column = int(boarding_pass[7:10].replace('L', '0').replace('R', '1'), 2)
	return row * 8 + column


print(get_seat_id(sorted(open('input.txt').readlines())[0]))

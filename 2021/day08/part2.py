
total = 0

for line in open('input.txt'):
	in_, out = map(str.split, line.split('|'))

	known_segments = {}

	for pattern in in_:
		match len(pattern):
			case 2:
				known_segments[1] = set(pattern)
			case 4:
				known_segments[4] = set(pattern)

	digits = ''

	for pattern in out:
		match len(pattern):
			case 2:
				digits += '1'
			case 4:
				digits += '4'
			case 3:
				digits += '7'
			case 7:
				digits += '8'
			case 5:
				if set(pattern).issuperset(known_segments[1]):
					digits += '3'
				elif len(set(pattern) & known_segments[4]) == 3:
					digits += '5'
				else:
					digits += '2'
			case 6:
				if not set(pattern).issuperset(known_segments[1]):
					digits += '6'
				elif set(pattern).issuperset(known_segments[4]):
					digits += '9'
				else:
					digits += '0'

	total += int(digits)

print(total)

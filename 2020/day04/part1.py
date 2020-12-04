
print(sum(
	all(required_field + ':' in passport for required_field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
	for passport in open('input.txt').read().split('\n\n')
))

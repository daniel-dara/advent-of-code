import re


def is_valid(passport: str) -> bool:
	# Parse fields.
	field_separator = r'(?:[ \n]|$)'
	byr = re.findall(r'byr:(\d+)' + field_separator, passport)
	iyr = re.findall(r'iyr:(\d+)' + field_separator, passport)
	eyr = re.findall(r'eyr:(\d+)' + field_separator, passport)
	hgt = re.findall(r'hgt:(\d+)(cm|in)' + field_separator, passport)
	hcl = re.findall(r'hcl:(#[0-9a-f]{6})' + field_separator, passport)
	ecl = re.findall(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)' + field_separator, passport)
	pid = re.findall(r'pid:(\d{9})' + field_separator, passport)

	# Verify all fields are present.
	if not all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
		return False

	# Cast values.
	byr = int(byr[0])
	iyr = int(iyr[0])
	eyr = int(eyr[0])
	hgt, hgt_unit = hgt[0]
	hgt = int(hgt)

	# Validate values.
	return (
		1920 <= byr <= 2002 and 2010 <= iyr <= 2020 <= eyr <= 2030 and
		(hgt_unit == 'in' and 59 <= hgt <= 76 or hgt_unit == 'cm' and 150 <= hgt <= 193)
	)


print(sum(map(is_valid, open('input.txt').read().split('\n\n'))))

#! /usr/bin/python
import sys
import os
import datetime

def createDirectory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
		print('Created folder: ./' + directory)

def normalizeDay(day):
	return day if len(day) == 2 else '0' + day

if len(sys.argv) == 1:
	print('Usage: setup.py [year=current] <day>')
	exit()
elif len(sys.argv) == 2:
	year = str(datetime.datetime.now().year)
	day = normalizeDay(sys.argv[1])
else:
	year = sys.argv[1]
	day = normalizeDay(sys.argv[2])

createDirectory(year)

dayPath = year + '/day' + day
createDirectory(dayPath)

for file in ['part1.py', 'part2.py', 'input.txt', 'sample.txt']:
	fullFilePath = dayPath + '/' + file
	
	if not os.path.exists(fullFilePath):
		open(fullFilePath, 'w').close()
		print('Created file: ' + fullFilePath)

print('done')

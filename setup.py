#! /usr/bin/python
import sys
import os

def createDirectory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

def normalizeDay(day):
	return day if len(day) == 2 else '0' + day

day = normalizeDay(sys.argv[1])
year = '2017'

createDirectory(year)

path = year + '/day' + day
createDirectory(path)

open(path + '/part1.py', 'w').close()
open(path + '/part2.py', 'w').close()
open(path + '/input.txt', 'w').close()
open(path + '/sample.txt', 'w').close()

print("Created files in: ", path)

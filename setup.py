#! /usr/bin/python
import shutil
import sys
import os
import datetime
from enum import Enum
from typing import List


class Action(Enum):
	CREATE_DIRECTORY = 0
	CREATE_EMPTY_FILE = 1
	COPY_CODE_FROM_TEMPLATE = 2


def create(path: str, action: Action) -> None:
	if os.path.exists(path):
		print('exists:', path)
	else:
		if action == Action.CREATE_DIRECTORY:
			os.makedirs(path)
		elif action == Action.CREATE_EMPTY_FILE:
			open(path, 'w')
		elif action == Action.COPY_CODE_FROM_TEMPLATE:
			shutil.copyfile('templates/template.py', path)
		else:
			raise ValueError('Unsupported action: ' + action.name)

		print('created:', path)


def main(args: List[str]) -> int:
	if len(args) == 1:
		print('Usage: setup.py [year=current] <day>')
		return 1
	elif len(args) == 2:
		year = str(datetime.datetime.now().year)
		day = args[1]
	elif len(args) == 3:
		year = args[1]
		day = args[2]
	else:
		raise ValueError(f'Too many arguments provided. Expected 1-2 but received {len(args) - 1}')

	create(year, Action.CREATE_DIRECTORY)

	problem_directory = f'{year}/day{day.zfill(2)}/'
	create(problem_directory, Action.CREATE_DIRECTORY)

	for file in 'part1', 'part2':
		file_path = problem_directory + file + '.py'
		create(file_path, Action.COPY_CODE_FROM_TEMPLATE)

	for file in 'example', 'input':
		file_path = problem_directory + file + '.txt'
		create(file_path, Action.CREATE_EMPTY_FILE)

	print('done!')
	return 0


exit(main(sys.argv))

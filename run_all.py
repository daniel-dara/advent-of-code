import os

working_dir = os.getcwd()

for path, _, filenames in os.walk(working_dir):
	for filename in filenames:
		if filename.endswith('.py') and 'day' in path and 'wip' not in path:
			print(path.split('advent-of-code')[1] + '\\' + filename)
			os.chdir(path.lstrip('.'))
			exec(open(filename).read())

import itertools
from itertools import groupby

filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [int(num) for num in fp.readline().split("-")]

def pairwise(iterable):
	a, b = itertools.tee(iterable)
	next(b, None)
	return zip(a, b)

same = [(str(i), str(i)) for i in range(10)]
def check_rules(num):
	s = str(num)
	if len(s) != 6:
		return 0
	p = list(pairwise(list(s)))
	for x, y in p:
		if x > y:
			return 0
	for pair in p:
		if pair in same:
			return 1
	return 0

def check_rules2(num):
	s = str(num)
	if len(s) != 6:
		return 0
	for x, y in list(pairwise(list(s))):
		if x > y:
			return 0
	groups = groupby(s)
	result = { label: sum(1 for _ in group) for label, group in groups }
	for key in result:
		if result[key] == 2:
			return 1
	return 0

def part1(arr):
	return sum([check_rules(val) for val in range(arr[0], arr[1])])

def part2(arr):
	return sum([check_rules2(val) for val in range(arr[0], arr[1])])

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = part1(arr.copy())
	print("part A:", result)
	result = part2(arr.copy())
	print("Part B:", result)


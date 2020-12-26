
filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [line.strip() for line in fp.readlines()]

def part1(arr):
	pass

def part2(arr):
	pass

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = part1(arr.copy())
	print("part A:", result)
	result = part2(arr.copy())
	print("Part B:", result)


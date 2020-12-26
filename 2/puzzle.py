
filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [int(num) for num in fp.readline().split(",")]

def create_dict(arr):
	return {i:val for (i, val) in enumerate(arr)}

def opcode(op, ipos1, ipos2, opos, arr):
	if op == 1:
		arr[opos] = arr[ipos1] + arr[ipos2]
	elif op == 2:
		arr[opos] = arr[ipos1] * arr[ipos2]
	return arr

def part1(arr, noun, verb):
	arr[1] = noun
	arr[2] = verb
	for i in range(len(arr))[::4]:
		op = arr[i]
		if op == 99 or op not in [1, 2] or len(arr) < i + 3:
			return arr[0]
		ipos1, ipos2, opos = arr[i+1], arr[i+2], arr[i+3]
		arr = opcode(op, ipos1, ipos2, opos, arr)

def part2(arr):
	goal = 19690720
	for noun in range(100):
		for verb in range(100):
			if part1(arr.copy(), noun, verb) == goal:
				return 100 * noun + verb

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = part1(arr.copy(), 12, 2)
	print("part A:", result)
	result = part2(arr.copy())
	print("Part B:", result)


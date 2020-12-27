
filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [line.strip().split(",") for line in fp.readlines()]

def calc_xy(d, dis, x, y):
	if d == "U":
		return x, y + dis
	elif d == "D":
		return x, y - dis
	elif d == "R":
		return x + dis, y
	elif d == "L":
		return x - dis, y

def get_steps(wire):
	steps = {}
	x, y = 0, 0
	s = 1
	for ins in wire:
		d, dis = ins[0], int(ins[1:])
		nx, ny = calc_xy(d, dis, x, y)

		rx = list(range(x+1, nx+1)) + list(range(x-1, nx-1, -1))
		for si, i in enumerate(rx):
			steps[f"{i} {y}"] = s + si

		ry = list(range(y+1, ny+1)) + list(range(y-1, ny-1, -1))
		for sj, j in enumerate(ry):
			steps[f"{x} {j}"] = s + sj

		s = s + len(rx) + len(ry)
		x, y = nx, ny
	return steps

def part1(arr):
	sl = [get_steps(wire) for wire in arr]
	common = [key for key in set(sl[0].keys()) & set(sl[1].keys())]
	return min([sum(map(abs, map(int, val.split()))) for val in common])

def part2(arr):
	sl = [get_steps(wire) for wire in arr]

	out = 9999999
	for key in sl[0]:
		if key in sl[1]:
			out = min(out, sl[0][key] + sl[1][key])
	return out

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = part1(arr.copy())
	print("part A:", result)
	result = part2(arr.copy())
	print("Part B:", result)
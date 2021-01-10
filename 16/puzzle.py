
filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [int(line) for line in fp.readlines()[0]]

def create_pattern(pattern, index, ilen):
	np = [index * [e] for e in pattern]
	flat_list = [item for sublist in np for item in sublist]
	out = flat_list
	while len(out) <= ilen:
		out += flat_list
	return flat_list

def mul(a):
	return a[0]*a[1]

def calc_phase(input, base_pattern, offset):
	out = []
	ilen = len(input)
	offset = offset % ilen
	for i in range(ilen):
		p = create_pattern(base_pattern, i+1, ilen)[offset:ilen+offset]
		l = list(map(mul, zip(input, p)))
		out.append(int(str(sum(l))[-1]))
	return out

def run_phases(input, base_pattern, phases):
	for i in range(phases):
		input = calc_phase(input, base_pattern, 1)
	return input

def part1(input):
	base_pattern = [0, 1, 0, -1]
	for i in range(100):
		input = calc_phase(input, base_pattern, 1)
	return "".join([str(i) for i in input[:8]])

def part2():
	input_string = open(filepath).readlines()[0]
	offset = int(input_string[:7], 10)
	input_list = list(map(int, input_string)) * 10000
	input_length = len(input_list)

	for i in range(100):
		partial_sum = sum(input_list[j] for j in range(offset, input_length))
		for j in range(offset, input_length):
			t = partial_sum
			partial_sum -= input_list[j]
			if t >= 0:
				input_list[j] = t % 10
			else:
				input_list[j] = (-t) % 10
	return "".join(map(str, input_list[offset: offset+8]))

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = part1(arr.copy())
	print("part A:", result)
	result = part2()
	print("Part B:", result)

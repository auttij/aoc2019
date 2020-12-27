
filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [int(num) for num in fp.readline().split(",")]

def create_dict(arr):
	return {i:val for (i, val) in enumerate(arr)}

def opcode(arr, op, a, b, c, *args):
	# ins = f"{a}{b}{c}{str(op).zfill(2)}"
	i1 = arr[args[0]] if c == "0" else args[0]
	if op == 4:
		# print("op4:", ins, i1)
		return i1

	if op == 3:
		# print("op3:", ins, args[0], args[1])
		arr[args[0]] = args[1]
		return arr
	i2 = arr[args[1]] if b == "0" else args[1]
	if op == 5:
		# print("op5:", ins, i1, i2)
		if i1 != 0:
			return i2
		else:
			return 0
	if op == 6:
		# print("op6:", ins, i1, i2)
		if i1 == 0:
			return i2
		else:
			return 0

	
	i3 = args[2]
	if op == 1:
		# print("op1:", ins, i1, i2, i3)
		arr[i3] = i1 + i2
	elif op == 2:
		# print("op2:", ins, i1, i2, i3)
		arr[i3] = i1 * i2
	elif op == 7:
		# print("op7:", ins, i1, i2, i3)
		if i1 < i2:
			arr[i3] = 1
		else:
			arr[i3] = 0
	elif op == 8:
		# print("op8:", ins, i1, i2, i3)
		if i1 == i2:
			arr[i3] = 1
		else:
			arr[i3] = 0

	return arr

def interpreter(arr):
	i = 0
	while True:
		s = arr[i]
		# print("i:", i, "s:", s)
		ins = list(str(s).zfill(5))
		insp = "".join(ins)
		a, b, c, d, e = ins
		op = int(d + e)
		if op == 99:
			return arr[0]
		elif op == 1 or op == 2 or op == 7 or op == 8:
			ipos1, ipos2, opos = arr[i+1], arr[i+2], arr[i+3]
			arr = opcode(arr, op, a, b, c, ipos1, ipos2, opos)
			i += 4
		elif op == 3:
			ipos = arr[i+1]
			val = int(input("give input: "))
			arr = opcode(arr, op, a, b, c, ipos, val)
			i += 2
		elif op == 4:
			ipos = arr[i+1]
			out = opcode(arr, op, a, b, c, ipos)
			if out != 0:
				return out
			i += 2
		elif op == 5:
			ipos1, ipos2 = arr[i+1], arr[i+2]
			out = opcode(arr, op, a, b, c, ipos1, ipos2)
			if out != 0:
				i = out
			else:
				i += 3
		elif op == 6:
			ipos1, ipos2 = arr[i+1], arr[i+2]
			out = opcode(arr, op, a, b, c, ipos1, ipos2)
			if out != 0:
				i = out
			else:
				i += 3
		else:
			print("something went wrong. op:", op)
			break
	return arr[0]

def part1(arr):
	return interpreter(arr)

def part2(arr):
	return interpreter(arr)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = part1(arr.copy())
	print("part A:", result)
	result = part2(arr.copy())
	print("Part B:", result)



filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [int(num) for num in list(fp.readlines()[0])]

def layers(arr, wid, hei):
	out, ls = [], wid*hei
	for li in range(len(arr[::ls])):
		l = arr[li*ls:(li+1)*ls]
		out.append([l[i*wid:(i+1)*wid] for i, v in enumerate(l[::wid])])
	return out

def part1(l):
	flats = [[i for sublist in layer for i in sublist] for layer in l]
	layer = [l for l in flats if l.count(0) == min([k.count(0) for k in flats])][0]
	return layer.count(1) * layer.count(2)

def part2(l):
	img = ""
	for j in range(len(l[0])):
		for i in range(len(l[0][0])):
			lrvs = [lr[j][i] for lr in l]
			while lrvs[0] == 2:
				lrvs = lrvs[1:]
			img += str(lrvs[0])
		img += "\n"
	img = img.replace("0", " ")
	img = img.replace("1", "#")
	return img

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	l = layers(arr, 25, 6)
	result = part1(l)
	print("part A:", result)
	result = part2(l)
	print(f"Part B:\n{result}")

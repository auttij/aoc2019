from math import floor

filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [line.strip() for line in fp.readlines()]

def get_fuel(mass):
	return floor(mass/3) - 2

def part1(arr):
	return sum([get_fuel(int(m)) for m in arr])

def get_fuel_fuel(mass):
	add = get_fuel(mass)
	prev_add, fuel_fuel = 0, 0
	while add > 0:
		fuel_fuel += add
		prev_add = add
		add = get_fuel(prev_add)
	return fuel_fuel

def part2(arr):
	return sum([get_fuel_fuel(int(m)) for m in arr])

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = part1(arr.copy())
	print("part A:", result)
	result = part2(arr.copy())
	print("Part B:", result)



filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [line.strip() for line in fp.readlines()]

def read_orbits(arr):
	orbits = { "COM": "COM" }
	for o in arr[0:]:
		a, b = o.split(")")
		orbits[b] = a
	return orbits

def get_route(orbits, orbit):
	route = []
	while orbit != "COM":
		route.append(orbit)
		orbit = orbits[orbit]
	return route

def part1(orbits):
	return sum([len(get_route(orbits, orbit)) for orbit in orbits])

def part2(orbits, start, goal):
	route1 = get_route(orbits, start)
	route2 = get_route(orbits, goal)
	common = [i for i in route1 if i in route2][0]
	route = route1[1:route1.index(common)] + [common] + route2[1:route2.index(common)][::-1]
	return len(route) - 1

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	orbits = read_orbits(arr)
	result = part1(orbits)
	print("part A:", result)
	result = part2(orbits, "YOU", "SAN")
	print("Part B:", result)


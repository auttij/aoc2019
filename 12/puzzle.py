from itertools import combinations
from math import gcd

filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [line.strip() for line in fp.readlines()]

def read_moons(arr):
	moons = {}
	coordinates = []
	for line in arr:
		coordinates.append(list(map(int, [i.split("=")[-1].strip() for i in line.split(",")])))
	return coordinates

def run_sim(coords, vel, steps=float('inf')):
	og_coords, og_vel = coords[:], vel[:]
	step = 0
	while step < steps and (not step or coords != og_coords or vel != og_vel):
		for i in range(len(coords)):
				vel[i] += sum(1 if coords[i] < pos else -1 for pos in coords if pos != coords[i])
		for i in range(len(coords)):
			coords[i] += vel[i]
		step += 1
	return step

def part1(coords):
    px, vx = [x for x, _, _ in coords], [0] * len(coords)
    py, vy = [y for _, y, _ in coords], [0] * len(coords)
    pz, vz = [z for _, _, z in coords], [0] * len(coords)
    for p, v in zip((px, py, pz), (vx, vy, vz)):
        run_sim(p, v, 1000)
    return sum((abs(px[i]) + abs(py[i]) + abs(pz[i])) * (abs(vx[i]) + abs(vy[i]) + abs(vz[i])) for i in range(len(coords)))

def part2(coords):
    def _lcm(a, b):
        return a * b // gcd(a, b)
    steps_x = run_sim([x for x, _, _ in coords], [0] * len(coords))
    steps_y = run_sim([y for _, y, _ in coords], [0] * len(coords))
    steps_z = run_sim([z for _, _, z in coords], [0] * len(coords))
    return _lcm(_lcm(steps_x, steps_y), steps_z)

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	result = part1(read_moons(arr))
	print("part A:", result)
	result = part2(read_moons(arr))
	print("Part B:", result)


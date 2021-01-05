from math import gcd, atan2, pi
import math
import operator

filepath = "./input.txt"
def read_file_to_arr(filepath):
	with open(filepath) as fp:
		return [line.strip() for line in fp.readlines()]

def asteroids(arr):
	ast = {}
	for yi, y in enumerate(arr):
		for xi, x in enumerate(y):
			if x == "#":
				ast[(xi, yi)] = "#"
	return ast

def dist(x1, y1, x2, y2):
	ax, ay = x2-x1, y2-y1
	g = gcd(ax, ay)
	return int(ax/g), int(ay/g)

def behind(i, p, l):
	xi, yi = i
	xp, yp = p
	xlen, ylen = l
	out = []
	xi += xp
	yi += yp
	while 0 <= xi and xi < xlen and 0 <= yi and yi < ylen:
		out.append((xi, yi))
		xi += xp
		yi += yp
	return out

def diff(li1, li2):
	li_dif = [i for i in li1 if i not in li2]
	return li_dif

def get_visible(ast, a, xlen, ylen):
		x, y = a
		others = [ai for ai in ast if ai != a]
		d = [dist(x, y, xi, yi) for xi, yi in others]
		b = [behind(others[i], p, (xlen, ylen)) for i, p in enumerate(d)]
		flat = [item for sublist in b for item in sublist]
		return diff(others, flat)


def part1(ast, xlen, ylen):
	visible = {}
	for a in ast:
		vis = get_visible(ast, a, xlen, ylen)
		visible[a] = len(vis)
	return max(visible, key=visible.get), visible[max(visible, key=visible.get)]

def ang(angle):
	x = angle - pi/2
	return x if x >= -pi else x + 2*pi

def part2(ast, res1, xlen, ylen):
	angles = {}
	a = res1[0]
	x, y = a
	vis = get_visible(ast, a, xlen, ylen)
	for v in vis:
		xi, yi = v
		dx, dy = xi-x, yi-y
		angle = ang(atan2(dy, dx))
		angles[v] = angle
	sor = [k for k, v in sorted(angles.items(), key=lambda item: item[1])]
	xv, xy = sor[199]
	return 100*xv + xy

if __name__ == "__main__":
	arr = read_file_to_arr(filepath)
	ast = asteroids(arr)
	result = part1(ast, len(arr[0]), len(arr))
	print("part A:", result)
	result = part2(ast, result, len(arr[0]), len(arr))
	print("Part B:", result)


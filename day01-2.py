#https://adventofcode.com/2016/day/1


def part2(input_file):
	with open(input_file, "r") as f:
		inp = f.read()

	inp2 = [(s[0], int(s[1:])) for s in inp.split(", ")]
	dirs = [0+1j, 1+0j, 0-1j, -1+0j]
	cur_dir = 0
	cur_pos = 0+0j
	seen = {cur_pos}
	for direction, num in inp2:
		cur_dir = (cur_dir + 2*(direction == "L") - 1) % 4
		for i in range(num):
			cur_pos += dirs[cur_dir]
			if cur_pos in seen:
				break
			seen.add(cur_pos)
		else:
			continue
		break
	return int(abs(cur_pos.imag) + abs(cur_pos.real))


def main():
	input_file = "day01-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
#https://adventofcode.com/2016/day/1


def part1(input_file):
	with open(input_file, "r") as f:
		sequence = f.read().strip().split(", ")

	pos = [0, 0]
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	cur_dir = (0, 1)

	for move in sequence:
		if move[0] == "R":
			cur_dir = directions[(directions.index(cur_dir) + 1) % 4]
		elif move[0] == "L":
			cur_dir = directions[(directions.index(cur_dir) - 1) % 4]
		steps = int(move[1:])
		pos[0] += steps * cur_dir[0]
		pos[1] += steps * cur_dir[1]

	return abs(pos[0]) + abs(pos[1])


def main():
	input_file = "day01-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
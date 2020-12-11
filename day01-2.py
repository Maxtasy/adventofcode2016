#https://adventofcode.com/2016/day/1


def part2(input_file):
  with open(input_file, "r") as f:
    sequence = f.read().strip().split(", ")

    pos = [0, 0]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_dir = (0, 1)

    visited = [[0, 0]]
    count = 0

    for move in sequence:
      count += 1

      if move[0] == "R":
        cur_dir = directions[(directions.index(cur_dir) + 1) % 4]
      elif move[0] == "L":
        cur_dir = directions[(directions.index(cur_dir) - 1) % 4]

      steps = int(move[1:])

      for _ in range(steps):
        pos[0] += cur_dir[0]
        pos[1] += cur_dir[1]

        if pos in visited:
          return abs(pos[0]) + abs(pos[1])
        else:
          visited.append(pos[:])


def main():
	input_file = "day01-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
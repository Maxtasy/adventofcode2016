#https://adventofcode.com/2016/day/20


def parse(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  ranges = []
  for line in lines:
    start, end = map(int, line.split("-"))
    ranges.append((start, end))

  return sorted(ranges)


def merge(ranges):
  merged = []

  for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:
      merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
      merged.append((start, end))

  return merged


def part1(input_file):
  ranges = parse(input_file)
  merged = merge(ranges)

  candidate = 0
  for start, end in merged:
    if start > candidate:
      return candidate
    candidate = max(candidate, end + 1)

  return candidate


def main():
  input_file = "day20-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

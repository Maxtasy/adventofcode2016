#https://adventofcode.com/2016/day/20


MAX_IP = 4294967295


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


def part2(input_file):
  ranges = parse(input_file)
  merged = merge(ranges)

  allowed = 0
  next_ip = 0

  for start, end in merged:
    if start > next_ip:
      allowed += start - next_ip
    next_ip = max(next_ip, end + 1)

  if next_ip <= MAX_IP:
    allowed += MAX_IP - next_ip + 1

  return allowed


def main():
  input_file = "day20-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()

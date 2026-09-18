#https://adventofcode.com/2016/day/22


import re
import itertools


NODE_RE = re.compile(r"node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T")


def parse(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  nodes = {}
  for line in lines:
    match = NODE_RE.search(line)
    if match:
      x, y, size, used, avail = map(int, match.groups())
      nodes[(x, y)] = (size, used, avail)

  return nodes


def part1(input_file):
  nodes = parse(input_file)

  count = 0
  for a, b in itertools.permutations(nodes, 2):
    size_a, used_a, avail_a = nodes[a]
    size_b, used_b, avail_b = nodes[b]
    if used_a > 0 and used_a <= avail_b:
      count += 1

  return count


def main():
  input_file = "day22-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

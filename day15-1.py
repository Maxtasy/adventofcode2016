#https://adventofcode.com/2016/day/15


import re
import itertools


DISC_RE = re.compile(r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)\.")


def parse(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  discs = []
  for line in lines:
    _, positions, start = map(int, DISC_RE.match(line).groups())
    discs.append((positions, start))

  return discs


def find_time(discs):
  for t in itertools.count():
    if all((start + t + i) % positions == 0 for i, (positions, start) in enumerate(discs, start=1)):
      return t


def part1(input_file):
  discs = parse(input_file)
  return find_time(discs)


def main():
  input_file = "day15-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

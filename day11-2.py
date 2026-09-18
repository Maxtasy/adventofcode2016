#https://adventofcode.com/2016/day/11


import re
import collections
import itertools


def parse_input(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  elements = {}

  for floor, line in enumerate(lines):
    for generator in re.findall(r"(\w+) generator", line):
      elements.setdefault(generator, {})["generator"] = floor
    for microchip in re.findall(r"(\w+)-compatible microchip", line):
      elements.setdefault(microchip, {})["microchip"] = floor

  pairs = [(item["microchip"], item["generator"]) for item in elements.values()]
  pairs.append((0, 0))
  pairs.append((0, 0))

  return pairs


def floor_valid(pairs, floor):
  generators = set(i for i, (chip, gen) in enumerate(pairs) if gen == floor)
  if not generators:
    return True

  for i, (chip, gen) in enumerate(pairs):
    if chip == floor and i not in generators:
      return False

  return True


def solve(pairs, num_floors=4):
  goal_floor = num_floors - 1
  start = (0, tuple(sorted(pairs)))

  visited = {start}
  queue = collections.deque([(start, 0)])

  while queue:
    (elevator, pairs_state), steps = queue.popleft()

    if elevator == goal_floor and all(chip == goal_floor and gen == goal_floor for chip, gen in pairs_state):
      return steps

    items_here = []
    for i, (chip, gen) in enumerate(pairs_state):
      if chip == elevator:
        items_here.append(("chip", i))
      if gen == elevator:
        items_here.append(("gen", i))

    combos = list(itertools.combinations(items_here, 1)) + list(itertools.combinations(items_here, 2))

    for combo in combos:
      for direction in (1, -1):
        new_floor = elevator + direction
        if new_floor < 0 or new_floor >= num_floors:
          continue

        new_pairs = list(pairs_state)
        for kind, i in combo:
          chip, gen = new_pairs[i]
          new_pairs[i] = (new_floor, gen) if kind == "chip" else (chip, new_floor)

        if not floor_valid(new_pairs, elevator) or not floor_valid(new_pairs, new_floor):
          continue

        new_state = (new_floor, tuple(sorted(new_pairs)))
        if new_state not in visited:
          visited.add(new_state)
          queue.append((new_state, steps + 1))

  return None


def part2(input_file):
  pairs = parse_input(input_file)
  return solve(pairs)


def main():
  input_file = "day11-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()

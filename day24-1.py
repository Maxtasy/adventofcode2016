#https://adventofcode.com/2016/day/24


import collections
import itertools


def parse(input_file):
  with open(input_file, "r") as f:
    grid = f.read().strip("\n").split("\n")

  locations = {}
  for y, row in enumerate(grid):
    for x, c in enumerate(row):
      if c.isdigit():
        locations[int(c)] = (x, y)

  return grid, locations


def bfs_distances(grid, start):
  distances = {start: 0}
  queue = collections.deque([start])

  while queue:
    x, y = queue.popleft()
    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
      if grid[ny][nx] != "#" and (nx, ny) not in distances:
        distances[(nx, ny)] = distances[(x, y)] + 1
        queue.append((nx, ny))

  return distances


def pairwise_distances(grid, locations):
  dists = {}
  for num, pos in locations.items():
    reachable = bfs_distances(grid, pos)
    for other_num, other_pos in locations.items():
      dists[(num, other_num)] = reachable[other_pos]

  return dists


def part1(input_file):
  grid, locations = parse(input_file)
  dists = pairwise_distances(grid, locations)

  numbers = [n for n in locations if n != 0]

  best = None
  for perm in itertools.permutations(numbers):
    route = (0,) + perm
    total = sum(dists[(route[i], route[i+1])] for i in range(len(route) - 1))
    if best is None or total < best:
      best = total

  return best


def main():
  input_file = "day24-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

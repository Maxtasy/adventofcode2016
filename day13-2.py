#https://adventofcode.com/2016/day/13


import collections


def is_open(x, y, favorite_number):
  value = x*x + 3*x + 2*x*y + y + y*y + favorite_number
  return bin(value).count("1") % 2 == 0


def part2(input_file, max_steps):
  with open(input_file, "r") as f:
    favorite_number = int(f.read().strip())

  start = (1, 1)
  visited = {start}
  queue = collections.deque([(start, 0)])

  while queue:
    (x, y), steps = queue.popleft()

    if steps == max_steps:
      continue

    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
      if nx < 0 or ny < 0:
        continue
      if (nx, ny) in visited:
        continue
      if not is_open(nx, ny, favorite_number):
        continue

      visited.add((nx, ny))
      queue.append(((nx, ny), steps + 1))

  return len(visited)


def main():
  input_file = "day13-input.txt"
  print(part2(input_file, 50))


if __name__ == "__main__":
  main()

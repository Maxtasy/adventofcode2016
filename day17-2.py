#https://adventofcode.com/2016/day/17


import hashlib
import collections


OPEN_CHARS = set("bcdef")
MOVES = [("U", 0, -1), ("D", 0, 1), ("L", -1, 0), ("R", 1, 0)]


def open_doors(passcode, path):
  digest = hashlib.md5((passcode + path).encode()).hexdigest()[:4]
  return [c in OPEN_CHARS for c in digest]


def part2(input_file):
  with open(input_file, "r") as f:
    passcode = f.read().strip()

  queue = collections.deque([(0, 0, "")])
  longest = 0

  while queue:
    x, y, path = queue.popleft()

    if (x, y) == (3, 3):
      longest = max(longest, len(path))
      continue

    doors = open_doors(passcode, path)

    for is_open, (direction, dx, dy) in zip(doors, MOVES):
      nx, ny = x + dx, y + dy
      if is_open and 0 <= nx <= 3 and 0 <= ny <= 3:
        queue.append((nx, ny, path + direction))

  return longest


def main():
  input_file = "day17-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()

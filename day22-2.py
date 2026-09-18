#https://adventofcode.com/2016/day/22


import re
import collections


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


def part2(nodes):
  max_x = max(x for x, y in nodes)
  max_y = max(y for x, y in nodes)

  empty_pos = next(pos for pos, (size, used, avail) in nodes.items() if used == 0)
  empty_size = nodes[empty_pos][0]

  walls = {pos for pos, (size, used, avail) in nodes.items() if used > empty_size}

  start_goal = (max_x, 0)
  target_goal = (0, 0)

  start = (empty_pos, start_goal)
  visited = {start}
  queue = collections.deque([(start, 0)])

  while queue:
    (empty, goal), steps = queue.popleft()

    if goal == target_goal:
      return steps

    ex, ey = empty
    for nx, ny in ((ex+1, ey), (ex-1, ey), (ex, ey+1), (ex, ey-1)):
      if not (0 <= nx <= max_x and 0 <= ny <= max_y):
        continue
      if (nx, ny) in walls:
        continue

      new_goal = empty if (nx, ny) == goal else goal
      new_state = ((nx, ny), new_goal)

      if new_state not in visited:
        visited.add(new_state)
        queue.append((new_state, steps + 1))

  return None


def main():
  input_file = "day22-input.txt"
  nodes = parse(input_file)
  print(part2(nodes))


if __name__ == "__main__":
  main()

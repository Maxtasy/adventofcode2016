#https://adventofcode.com/2016/day/19


import collections


def winning_elf(n):
  left = collections.deque(range(1, n // 2 + 1))
  right = collections.deque(range(n // 2 + 1, n + 1))

  while len(left) + len(right) > 1:
    if len(left) > len(right):
      left.pop()
    else:
      right.popleft()

    right.append(left.popleft())
    left.append(right.popleft())

  return left[0] if left else right[0]


def part2(input_file):
  with open(input_file, "r") as f:
    n = int(f.read().strip())

  return winning_elf(n)


def main():
  input_file = "day19-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()

#https://adventofcode.com/2016/day/19


def winning_elf(n):
  power = 1
  while power * 2 <= n:
    power *= 2

  return 2 * (n - power) + 1


def part1(input_file):
  with open(input_file, "r") as f:
    n = int(f.read().strip())

  return winning_elf(n)


def main():
  input_file = "day19-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

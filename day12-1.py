#https://adventofcode.com/2016/day/12


def parse(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  return [line.split() for line in lines]


def value(registers, x):
  return registers[x] if x in registers else int(x)


def run(instructions, registers):
  i = 0

  while i < len(instructions):
    op, *args = instructions[i]

    if op == "cpy":
      x, y = args
      registers[y] = value(registers, x)
      i += 1
    elif op == "inc":
      registers[args[0]] += 1
      i += 1
    elif op == "dec":
      registers[args[0]] -= 1
      i += 1
    elif op == "jnz":
      x, y = args
      i += int(y) if value(registers, x) != 0 else 1

  return registers


def part1(input_file):
  instructions = parse(input_file)
  registers = {"a": 0, "b": 0, "c": 0, "d": 0}
  registers = run(instructions, registers)
  return registers["a"]


def main():
  input_file = "day12-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

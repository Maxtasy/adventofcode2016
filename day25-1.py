#https://adventofcode.com/2016/day/25


import itertools


def parse(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  return [line.split() for line in lines]


def value(registers, x):
  return registers[x] if x in registers else int(x)


def produces_clock_signal(instructions, a, required_outputs=50, max_steps=1000000):
  registers = {"a": a, "b": 0, "c": 0, "d": 0}
  i = 0
  steps = 0
  outputs = []

  while i < len(instructions) and steps < max_steps and len(outputs) < required_outputs:
    steps += 1
    op = instructions[i]
    name, args = op[0], op[1:]

    if name == "cpy":
      x, y = args
      if y in registers:
        registers[y] = value(registers, x)
      i += 1
    elif name == "inc":
      if args[0] in registers:
        registers[args[0]] += 1
      i += 1
    elif name == "dec":
      if args[0] in registers:
        registers[args[0]] -= 1
      i += 1
    elif name == "jnz":
      x, y = args
      i += value(registers, y) if value(registers, x) != 0 else 1
      continue
    elif name == "out":
      out_val = value(registers, args[0])
      if out_val != len(outputs) % 2:
        return False
      outputs.append(out_val)
      i += 1

  return len(outputs) == required_outputs


def part1(input_file):
  instructions = parse(input_file)

  for a in itertools.count(0):
    if produces_clock_signal(instructions, a):
      return a


def main():
  input_file = "day25-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

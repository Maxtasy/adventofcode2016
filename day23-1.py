#https://adventofcode.com/2016/day/23


def parse(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  return [line.split() for line in lines]


def value(registers, x):
  return registers[x] if x in registers else int(x)


def toggle(op):
  if len(op) == 2:
    return ["dec" if op[0] == "inc" else "inc", op[1]]
  else:
    return ["cpy" if op[0] == "jnz" else "jnz"] + op[1:]


def run(instructions, registers):
  instructions = [list(op) for op in instructions]
  i = 0

  while i < len(instructions):
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
    elif name == "tgl":
      target = i + value(registers, args[0])
      if 0 <= target < len(instructions):
        instructions[target] = toggle(instructions[target])
      i += 1

  return registers


def part1(input_file):
  instructions = parse(input_file)
  registers = {"a": 7, "b": 0, "c": 0, "d": 0}
  registers = run(instructions, registers)
  return registers["a"]


def main():
  input_file = "day23-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

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


def multiply_add_loop(instructions, i, registers):
  if i + 6 > len(instructions):
    return None

  ops = instructions[i:i+6]
  if [op[0] for op in ops] != ["cpy", "inc", "dec", "jnz", "dec", "jnz"]:
    return None

  cpy_op, inc_op, dec_op, jnz_op, dec2_op, jnz2_op = ops
  b, c1 = cpy_op[1], cpy_op[2]
  a = inc_op[1]
  c2 = dec_op[1]
  c3, off1 = jnz_op[1], jnz_op[2]
  d1 = dec2_op[1]
  d2, off2 = jnz2_op[1], jnz2_op[2]

  if c1 != c2 or c2 != c3 or off1 != "-2":
    return None
  if d1 != d2 or off2 != "-5":
    return None
  if a not in registers or c1 not in registers or d1 not in registers:
    return None
  if a == c1 or a == d1 or c1 == d1:
    return None

  return a, b, c1, d1


def multiply_loop(instructions, i, registers):
  if i + 2 >= len(instructions):
    return None

  op1, op2, op3 = instructions[i], instructions[i+1], instructions[i+2]

  if op3[0] != "jnz" or op3[2] != "-2":
    return None

  incs = [op for op in (op1, op2) if op[0] == "inc"]
  decs = [op for op in (op1, op2) if op[0] == "dec"]

  if len(incs) != 1 or len(decs) != 1:
    return None

  target, counter = incs[0][1], decs[0][1]

  if op3[1] != counter or target == counter:
    return None
  if target not in registers or counter not in registers:
    return None

  return target, counter


def run(instructions, registers):
  instructions = [list(op) for op in instructions]
  i = 0

  while i < len(instructions):
    add_loop = multiply_add_loop(instructions, i, registers)
    if add_loop:
      a, b, c, d = add_loop
      registers[a] += value(registers, b) * registers[d]
      registers[c] = 0
      registers[d] = 0
      i += 6
      continue

    loop = multiply_loop(instructions, i, registers)
    if loop:
      target, counter = loop
      registers[target] += registers[counter]
      registers[counter] = 0
      i += 3
      continue

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


def part2(input_file):
  instructions = parse(input_file)
  registers = {"a": 12, "b": 0, "c": 0, "d": 0}
  registers = run(instructions, registers)
  return registers["a"]


def main():
  input_file = "day23-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()

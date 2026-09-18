#https://adventofcode.com/2016/day/21


def swap_position(chars, x, y):
  chars[x], chars[y] = chars[y], chars[x]


def swap_letter(chars, a, b):
  x, y = chars.index(a), chars.index(b)
  swap_position(chars, x, y)


def rotate(chars, steps):
  steps %= len(chars)
  chars[:] = chars[-steps:] + chars[:-steps]


def rotate_based_on_letter(chars, letter):
  index = chars.index(letter)
  steps = 1 + index + (1 if index >= 4 else 0)
  rotate(chars, steps)


def rotate_based_on_letter_inverse(chars, letter):
  target = chars[:]

  for shift in range(len(chars)):
    candidate = target[:]
    rotate(candidate, -shift)
    test = candidate[:]
    rotate_based_on_letter(test, letter)
    if test == target:
      chars[:] = candidate
      return


def reverse_positions(chars, x, y):
  chars[x:y+1] = chars[x:y+1][::-1]


def move_position(chars, x, y):
  c = chars.pop(x)
  chars.insert(y, c)


def apply_instruction_reverse(chars, line):
  parts = line.split()

  if parts[0] == "swap" and parts[1] == "position":
    swap_position(chars, int(parts[2]), int(parts[5]))
  elif parts[0] == "swap" and parts[1] == "letter":
    swap_letter(chars, parts[2], parts[5])
  elif parts[0] == "rotate" and parts[1] in ("left", "right"):
    steps = int(parts[2])
    rotate(chars, -steps if parts[1] == "right" else steps)
  elif parts[0] == "rotate" and parts[1] == "based":
    rotate_based_on_letter_inverse(chars, parts[6])
  elif parts[0] == "reverse":
    reverse_positions(chars, int(parts[2]), int(parts[4]))
  elif parts[0] == "move":
    move_position(chars, int(parts[5]), int(parts[2]))


def part2(input_file, password):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  chars = list(password)

  for line in reversed(lines):
    apply_instruction_reverse(chars, line)

  return "".join(chars)


def main():
  input_file = "day21-input.txt"
  print(part2(input_file, "fbgdceah"))


if __name__ == "__main__":
  main()

#https://adventofcode.com/2016/day/18


def next_row(row):
  padded = "." + row + "."
  return "".join(
    "^" if padded[i] != padded[i+2] else "."
    for i in range(len(row))
  )


def count_safe_tiles(first_row, num_rows):
  safe_count = 0
  row = first_row

  for _ in range(num_rows):
    safe_count += row.count(".")
    row = next_row(row)

  return safe_count


def part2(input_file, num_rows):
  with open(input_file, "r") as f:
    first_row = f.read().strip()

  return count_safe_tiles(first_row, num_rows)


def main():
  input_file = "day18-input.txt"
  print(part2(input_file, 400000))


if __name__ == "__main__":
  main()

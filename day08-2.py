#https://adventofcode.com/2016/day/8


import collections


GRID_ROWS = 6
GRID_COLS = 50


def part2(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    grid = [collections.deque("." for j in range(GRID_COLS)) for i in range(GRID_ROWS)]

    for line in lines:
      line_parts = line.split()
      if line_parts[0] == "rect":
        cols, rows = list(map(int, line_parts[1].split("x")))
        for row in range(rows):
          for col in range(cols):
            grid[row][col] = "#"
      elif line_parts[0] == "rotate":
        if line_parts[1] == "column":
          col = int(line_parts[2][2:])
          amount = int(line_parts[-1])

          column = collections.deque()
          for row in range(len(grid)):
            column.append(grid[row][col])
          
          column.rotate(amount)

          for row in range(len(grid)):
            grid[row][col] = column[row]
        elif line_parts[1] == "row":
          row = int(line_parts[2][2:])
          amount = int(line_parts[-1])

          grid[row].rotate(amount)
    
    for row in grid:
      print("".join(row))


def main():
  input_file = "day08-input.txt"
  part2(input_file)


if __name__ == "__main__":
  main()
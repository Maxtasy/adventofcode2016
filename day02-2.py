#https://adventofcode.com/2016/day/2


KEYPAD = [
  [False, False, "1", False, False],
  [False, "2", "3", "4", False],
  ["5", "6", "7", "8", "9"],
  [False, "A", "B", "C", False],
  [False, False, "D", False, False],
  ]


def part2(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    cur_row = 2
    cur_col = 0

    keypad_rows = len(KEYPAD)
    keypad_cols = len(KEYPAD)

    code = []

    for line in lines:
      for i in range(len(line)):
        char = line[i]

        if char == "U":
          candidate = cur_row - 1
          if candidate >= 0 and KEYPAD[candidate][cur_col] != False:
            cur_row = candidate
        elif char == "D":
          candidate = cur_row + 1
          if candidate < keypad_rows and KEYPAD[candidate][cur_col] != False:
            cur_row = candidate
        elif char == "L":
          candidate = cur_col - 1
          if candidate >= 0 and KEYPAD[cur_row][candidate] != False:
            cur_col = candidate
        elif char == "R":
          candidate = cur_col + 1
          if candidate < keypad_cols and KEYPAD[cur_row][candidate] != False:
            cur_col = candidate
        else:
          print("Unexpected direction", char)
          return
        
        if i == len(line) - 1:
          code.append(KEYPAD[cur_row][cur_col])
    
    return "".join(code)


def main():
	input_file = "day02-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()
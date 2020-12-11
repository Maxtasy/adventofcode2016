#https://adventofcode.com/2016/day/2


KEYPAD = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    cur_row = 1
    cur_col = 1

    keypad_rows = len(KEYPAD)
    keypad_cols = len(KEYPAD)

    code = []

    for line in lines:
      for i in range(len(line)):
        char = line[i]

        if char == "U":
          cur_row = max(cur_row - 1, 0)
        elif char == "D":
          cur_row = min(cur_row + 1, keypad_rows - 1)
        elif char == "L":
          cur_col = max(cur_col - 1, 0)
        elif char == "R":
          cur_col = min(cur_col + 1, keypad_cols - 1)
        else:
          print("Unexpected direction", char)
          return
        
        if i == len(line) - 1:
          code.append(KEYPAD[cur_row][cur_col])
    
    return int("".join(code))


def main():
	input_file = "day02-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
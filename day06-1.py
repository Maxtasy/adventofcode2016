#https://adventofcode.com/2016/day/6


from collections import defaultdict


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    letter_counts = [defaultdict(int) for i in range(len(lines[0]))]

    for line in lines:
      for i in range(len(line)):
        letter_counts[i][line[i]] += 1
    
    result = ""

    for i in range(len(letter_counts)):
      most = 0
      for key in letter_counts[i]:
        if letter_counts[i][key] > most:
          letter = key
          most = letter_counts[i][key]
      
      result += letter
    
    return result


def main():
  input_file = "day06-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
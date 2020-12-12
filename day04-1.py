#https://adventofcode.com/2016/day/4


from collections import defaultdict


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    sector_id_sum = 0

    for i in range(len(lines)):
      line_parts = lines[i].split("-")
      sector_id, checksum = line_parts[-1][:-1].split("[")
      sector_id = int(sector_id)

      chars = defaultdict(int)

      x = 0

      for line_part in line_parts[:-1]:
        for char in line_part:
          chars[char] += 1
          if char not in checksum:
            # Most occurrences of a character that is not present in checksum
            x = max(chars[char], x)

      real = True

      # loop over all characters in checksum
      for i in range(len(checksum)):
        current_char = checksum[i]
        if i == 0:
          if chars[current_char] < x:
            real = False
            break
          else:
            continue

        previous_char = checksum[i-1]

        if chars[current_char] < x:
          real = False
          break
        
        if chars[current_char] > chars[previous_char]:
          real = False
          break

        if chars[current_char] == chars[previous_char]:
          if current_char < previous_char:
            real = False
            break
      
      # if the room is still real, add sector id to sum
      if real:
        sector_id_sum += sector_id

    return sector_id_sum


def main():
	input_file = "day04-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
#https://adventofcode.com/2016/day/7


def is_abba(string):
  return ((string[0] != string[1]) and 
          (string[2] == string[1]) and 
          (string[3] == string[0]))


def part1(input_file):
  with open(input_file, "r") as f:
    ips = f.read().strip().split("\n")

    valid_count = 0

    for ip in ips:
      has_abba = False
      inside_brackets = False

      for i in range(len(ip) - 3):
        if ip[i-1] == "[":
          inside_brackets = True
        elif ip[i-1] == "]":
          inside_brackets = False

        sub_str = ip[i:i+4]
        
        if inside_brackets:
          if is_abba(sub_str):
            has_abba = False
            break
        elif not has_abba:
          if is_abba(sub_str):
            has_abba = True
      
      if has_abba:
        valid_count += 1

    return valid_count


def main():
  input_file = "day07-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
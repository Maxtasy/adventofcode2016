#https://adventofcode.com/2016/day/7


def is_aba(string):
  return ((string[0] != string[1]) and 
          (string[2] == string[0]) and 
          ("[" not in string) and
          ("]" not in string))


def part2(input_file):
  with open(input_file, "r") as f:
    ips = f.read().strip().split("\n")

    valid_count = 0

    for ip in ips:
      matching_babs = []
      matching_abas = []
      inside_brackets = False

      for i in range(len(ip) - 2):
        if ip[i-1] == "[":
          inside_brackets = True
        elif ip[i-1] == "]":
          inside_brackets = False

        sub_str = ip[i:i+3]
        
        if inside_brackets:
          if is_aba(sub_str):
            if sub_str in matching_babs:
              valid_count += 1
              break
            else:
              matching_abas.append(sub_str[1]+sub_str[0]+sub_str[1])
        else:
          if is_aba(sub_str):
            if sub_str in matching_abas:
              valid_count += 1
              break
            else:
              matching_babs.append(sub_str[1]+sub_str[0]+sub_str[1])

    return valid_count


def main():
  input_file = "day07-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
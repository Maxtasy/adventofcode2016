#https://adventofcode.com/2016/day/9


def decompressed_length(data):
  length = 0
  i = 0
  while i < len(data):
    if data[i] == "(":
      end = data.index(")", i)
      chars, repeat = list(map(int, data[i+1:end].split("x")))
      length += decompressed_length(data[end+1:end+1+chars]) * repeat
      i = end + 1 + chars
    else:
      length += 1
      i += 1

  return length


def part2(input_file):
  with open(input_file, "r") as f:
    data = f.read().strip()
    return decompressed_length(data)


def main():
  input_file = "day09-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()

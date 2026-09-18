#https://adventofcode.com/2016/day/16


def dragon_curve(data, length):
  while len(data) < length:
    b = "".join("1" if c == "0" else "0" for c in reversed(data))
    data = data + "0" + b

  return data[:length]


def checksum(data):
  while len(data) % 2 == 0:
    data = "".join("1" if data[i] == data[i+1] else "0" for i in range(0, len(data), 2))

  return data


def part1(input_file, disk_length):
  with open(input_file, "r") as f:
    initial_state = f.read().strip()

  data = dragon_curve(initial_state, disk_length)
  return checksum(data)


def main():
  input_file = "day16-input.txt"
  print(part1(input_file, 272))


if __name__ == "__main__":
  main()

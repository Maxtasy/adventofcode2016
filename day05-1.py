#https://adventofcode.com/2016/day/5


import hashlib


def part1(input_file):
  with open(input_file, "r") as f:
    door_id = f.read().strip()

    password = ""

    index = 0
    while len(password) < 8:
      to_be_hashed = door_id + str(index)
      hashed = str(hashlib.md5(to_be_hashed.encode("utf-8")).hexdigest())
      if hashed[:5] == "00000":
        password += hashed[5]
        print("Found:", password)
      index += 1
      
    return password


def main():
  input_file = "day05-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()
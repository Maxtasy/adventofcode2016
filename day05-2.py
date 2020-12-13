#https://adventofcode.com/2016/day/5


import hashlib


def part2(input_file):
  with open(input_file, "r") as f:
    door_id = f.read().strip()

    password = "________"

    index = 0
    while True:
      to_be_hashed = door_id + str(index)
      hashed = str(hashlib.md5(to_be_hashed.encode("utf-8")).hexdigest())
      if hashed[:5] == "00000" and hashed[5].isnumeric():
        position = int(hashed[5])
        if ((position >= 0) and 
            (position < len(password)) and 
            (password[position] == "_")):
          char = hashed[6]
          password = password[:position] + char + password[position+1:]
          print("Found:", password)
          if "_" not in password:
            break
      index += 1
      
    return password


def main():
  input_file = "day05-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()
#https://adventofcode.com/2016/day/14


import hashlib
import re


TRIPLET_RE = re.compile(r"(.)\1\1")


def find_64th_key_index(salt, stretch=0):
  hash_cache = {}

  def get_hash(i):
    if i not in hash_cache:
      h = hashlib.md5((salt + str(i)).encode()).hexdigest()
      for _ in range(stretch):
        h = hashlib.md5(h.encode()).hexdigest()
      hash_cache[i] = h
    return hash_cache[i]

  found_keys = []
  i = 0

  while len(found_keys) < 64:
    h = get_hash(i)
    match = TRIPLET_RE.search(h)

    if match:
      quintuplet = match.group(1) * 5
      if any(quintuplet in get_hash(i + j) for j in range(1, 1001)):
        found_keys.append(i)

    i += 1

  return found_keys[63]


def part1(input_file):
  with open(input_file, "r") as f:
    salt = f.read().strip()

  return find_64th_key_index(salt)


def main():
  input_file = "day14-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()

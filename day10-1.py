#https://adventofcode.com/2016/day/10


import re
import collections


VALUE_RE = re.compile(r"value (\d+) goes to bot (\d+)")
BOT_RE = re.compile(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")


def parse(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

  initial_values = []
  instructions = {}

  for line in lines:
    value_match = VALUE_RE.match(line)
    if value_match:
      value, bot = map(int, value_match.groups())
      initial_values.append((value, bot))
      continue

    bot_match = BOT_RE.match(line)
    bot, low_type, low_num, high_type, high_num = bot_match.groups()
    instructions[int(bot)] = (low_type, int(low_num), high_type, int(high_num))

  return initial_values, instructions


def part1(input_file, target_low, target_high):
  initial_values, instructions = parse(input_file)

  bots = collections.defaultdict(list)
  outputs = {}

  for value, bot in initial_values:
    bots[bot].append(value)

  while True:
    ready = [bot for bot, values in bots.items() if len(values) == 2]
    if not ready:
      break

    for bot in ready:
      low, high = sorted(bots[bot])
      bots[bot] = []

      if low == target_low and high == target_high:
        return bot

      low_type, low_num, high_type, high_num = instructions[bot]

      if low_type == "bot":
        bots[low_num].append(low)
      else:
        outputs[low_num] = low

      if high_type == "bot":
        bots[high_num].append(high)
      else:
        outputs[high_num] = high


def main():
  input_file = "day10-input.txt"
  print(part1(input_file, 17, 61))


if __name__ == "__main__":
  main()

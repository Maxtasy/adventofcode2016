#https://adventofcode.com/2016/day/3


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    triangles = []

    for line in lines:
      triangle = []

      line_parts = line.split(" ")
      for part in line_parts:
        if part != "":
          triangle.append(int(part))
      
      triangles.append(triangle)
    
    valid_triangles = 0

    for triangle in triangles:
      valid = True
      for i in range(len(triangle)):
        if sum(triangle) - triangle[i] <= triangle[i]:
          valid = False
          break
      
      if valid:
        valid_triangles += 1
    
    return valid_triangles


def main():
	input_file = "day03-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()
#https://adventofcode.com/2016/day/3


def part2(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    triangles = []

    triangle1 = []
    triangle2 = []
    triangle3 = []

    for i in range(len(lines)):
      line_parts = lines[i].split(" ")

      cleaned_line = []

      for part in line_parts:
        if part != "":
          cleaned_line.append(int(part))

      triangle1.append(cleaned_line[0])
      triangle2.append(cleaned_line[1])
      triangle3.append(cleaned_line[2])

      if len(triangle1) == 3:
        triangles.append(triangle1[:])
        triangles.append(triangle2[:])
        triangles.append(triangle3[:])
        triangle1 = []
        triangle2 = []
        triangle3 = []
    
    print(triangles)
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
	print(part2(input_file))


if __name__ == "__main__":
	main()
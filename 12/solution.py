sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

directions = [
  (-1, 0),
  (0, -1),
  (1, 0),
  (0, 1)
]

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def solve(input):
  price = 0
  visited = set()

  for row in range(len(input)):
    for col in range(len(input[0])):
      node = (row, col)
      if node in visited: continue

      letter = input[row][col]
      stack = [node]
      visited.add((node))
      area = 0
      perimeter = 0

      while len(stack) > 0:
        node = stack.pop()
        area += 1
        for (dx, dy) in directions:
          nx, ny = node[0] + dx, node[1] + dy

          if (nx, ny) in visited: 
            if input[nx][ny] != letter: perimeter += 1
            continue

          if nx >= 0 and nx < len(input) and ny >= 0 and ny < len(input[0]) and input[nx][ny] == letter:
            visited.add((nx, ny))
            stack.append((nx, ny))
          else:
            perimeter += 1

      price += (area * perimeter)

  print('Part 1 Result:', price)

  price = 0
  visited = set()
  for row in range(len(input)):
    for col in range(len(input[0])):
      node = (row, col)
      if node in visited: continue

      letter = input[row][col]
      stack = [node]
      visited.add((node))
      area = 0
      perimeter = 0
      
      perimeters = {}
      for direction in directions:
        perimeters[direction] = set()

      while len(stack) > 0:
        node = stack.pop()
        area += 1
        for (dx, dy) in directions:
          nx, ny = node[0] + dx, node[1] + dy

          if (nx, ny) in visited: 
            if input[nx][ny] != letter: perimeters[(dx, dy)].add((nx, ny))
            continue

          if nx >= 0 and nx < len(input) and ny >= 0 and ny < len(input[0]) and input[nx][ny] == letter:
            visited.add((nx, ny))
            stack.append((nx, ny))
          else:
            perimeters[(dx, dy)].add((nx, ny))

      # print(letter)
      for direction, borders in perimeters.items():
        # Grab a random border
        # print(direction, borders)
        while len(borders) > 0:
          border = borders.pop()
          queue = [border]
          # Find all related borders

          while len(queue) > 0:
            x, y = queue.pop()
            
            # We looked north/south for this border, so check to its left and right
            if direction == (-1, 0) or direction == (1, 0):
              if (x, y-1) in borders:
                borders.discard((x, y-1))
                queue.append((x, y-1))
              if (x, y+1) in borders:
                borders.discard((x, y+1))
                queue.append((x, y+1))
            # Otherwise look up and down
            else:
              if (x-1, y) in borders:
                borders.discard((x-1, y))
                queue.append((x-1, y))
              if (x+1, y) in borders:
                borders.discard((x+1, y))
                queue.append((x+1, y))
          
          perimeter += 1

      price += (area * perimeter)

  print('Part 2 Result:', price)

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve(sampleInput)
print("------------------")
print("Puzzle")
solve(puzzleInput)
print("------------------")
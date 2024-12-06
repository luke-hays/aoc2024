sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def printGrid(grid):
  for row in grid:
    print(row)

def analyzePath(input, originalPos, detectCycles, newObstacle):
  cycles = 0
  i, j = newObstacle if detectCycles else [0, 0]

  pos = [originalPos[0], originalPos[1]]
  memo = set()
  direction = 'n'

  while True:
    newPos = (pos[0], pos[1], direction) if detectCycles else (pos[0], pos[1])
    
    if detectCycles and newPos in memo:
      cycles += 1
      break

    memo.add(newPos)

    x, y = pos[0], pos[1]
    if direction == 'n':
      x -= 1
    elif direction == 'e':
      y += 1
    elif direction == 's':
      x += 1
    elif direction == 'w':
      y -= 1

    if x < 0 or x >= len(input) or y < 0 or y >= len(input[0]):
      break

    if input[x][y] == '#' or (detectCycles and x == i and y == j):
      if direction == 'n':
        direction = 'e'
        x += 1
      elif direction == 'e':
        direction = 's'
        y -= 1
      elif direction == 's':
        direction = 'w'
        x -= 1
      elif direction == 'w':
        direction = 'n'
        y += 1
    
    pos = [x, y]
  
  return cycles if detectCycles else memo

def solve(input):
  result2 = 0

  originalPos = []
  for i in range(len(input)):
    for j in range(len(input[i])):
      if input[i][j] == '^': originalPos = [i, j]

  paths = analyzePath(input, originalPos, False, [])
  print("Result 1: ", len(paths))

  for path in paths:
    i, j = path
    if input[i][j] == '#' or input[i][j] == '^': continue
    result2 += analyzePath(input, originalPos, True, [i, j])

  print("Result 2: ", result2)
  
sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve(sampleInput)
print("------------------")
print("Puzzle")
solve(puzzleInput)
print("------------------")

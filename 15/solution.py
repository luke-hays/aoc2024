sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def parseInput(input):
  grid = []
  instructions = []
  robot = None

  i = 0
  while i < len(input):
    grid.append([c for c in input[i]])
    i += 1
    if input[i] == '':
      i += 1
      break
  while i < len(input):
    for instruction in list(input[i]):
      instructions.append(instruction)
    i += 1

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == '@':
        robot = [row, col]
        break
    if robot != None: break

  return (grid, instructions, robot)

def moveObject(grid, obj, instruction):
  nx, ny = obj

  if instruction == '<':
    ny -= 1
  elif instruction == '^':
    nx -= 1
  elif instruction == '>':
    ny += 1
  elif instruction == 'v':
    nx += 1

  if grid[nx][ny] == '#':
    return
  
  if grid[nx][ny] == '.':
    return [nx, ny]

  newPos = moveObject(grid, [nx, ny], instruction)

  if newPos:
    grid[newPos[0]][newPos[1]] = grid[nx][ny]
    return [nx, ny]

  return

def calculateGpsSum(grid):
  gps = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 'O':
        gps += (100 * r + c)
  return gps
  
def solve1(inp):
  grid, instructions, robot = parseInput(inp)

  for instruction in instructions:
    newPos = moveObject(grid, robot, instruction)
    if newPos:
      grid[newPos[0]][newPos[1]] = '@'
      grid[robot[0]][robot[1]] = '.'
      robot = newPos

  print('GPS Sum: {0}'.format(calculateGpsSum(grid)))

def scaledParse(inp):
  grid = []
  instructions = []
  robot = None

  i = 0
  while i < len(inp):
    if inp[i] == '': break

    line = []
    for c in inp[i]:
      if c == '#' or c == '.':
        line.append(c)
        line.append(c)
      if c == 'O':
        line.append('[')
        line.append(']')
      if c == '@':
        line.append('@')
        line.append('.')
    grid.append(line)
    i += 1

  i += 1
  while i < len(inp):
    for instruction in list(inp[i]):
      instructions.append(instruction)
    i += 1

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == '@':
        robot = [row, col]
        break
    if robot != None: break

  return (grid, instructions, robot)

def scaledMoveObject(grid, obj, instruction):
  nx, ny = obj

  if instruction == '<':
    ny -= 1
  elif instruction == '^':
    nx -= 1
  elif instruction == '>':
    ny += 1
  elif instruction == 'v':
    nx += 1

  if grid[nx][ny] == '#':
    return
  
  if (instruction == '^' or instruction == 'v') and (grid[nx][ny] == '[' or grid[nx][ny] == ']'):
    ax, ay = nx, ny
    bx, by = nx, ny

    if grid[nx][ny] == '[':
      by += 1
    else:
      by -= 1
    
    newPosA = scaledMoveObject(grid, [ax, ay], instruction)
    newPosB = scaledMoveObject(grid, [bx, by], instruction)

    if newPosA and newPosB:
      grid[newPosA[0]][newPosA[1]] = grid[ax][ay]
      grid[newPosB[0]][newPosB[1]] = grid[bx][by]
      grid[bx][by] = '.'
      return [nx, ny]
    return
  
  if grid[nx][ny] == '.':
    return [nx, ny]
  
  newPos = scaledMoveObject(grid, [nx, ny], instruction)

  if newPos:
    grid[newPos[0]][newPos[1]] = grid[nx][ny]
    return [nx, ny]

  return


# Not a great solution but I don't have time today.
def solve2(inp):
  grid, instructions, robot = scaledParse(inp)
  for instruction in instructions:
    copyGrid = [[c for c in line] for line in grid]
    
    newPos = scaledMoveObject(copyGrid, robot, instruction)
    if newPos:
      copyGrid[newPos[0]][newPos[1]] = '@'
      copyGrid[robot[0]][robot[1]] = '.'
      robot = newPos
  
    valid = True
    for i in range(len(copyGrid)):
      for j in range(len(copyGrid[0])):
        if copyGrid[i][j] == '[' and copyGrid[i][j+1] != ']':
          valid = False
          break
        if copyGrid[i][j] == ']' and copyGrid[i][j-1] != '[':
          valid = False
          break
      if not valid:
        break

    if valid: grid = copyGrid

    # # for row in grid:
    # #   print(''.join(row))

    # print()
  
  gps = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == '[':
        gps += (100 * r + c)
  print('GPS Sum: {0}'.format(gps))

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve1(sampleInput)
solve2(sampleInput)
print("------------------")
print("Puzzle")
solve1(puzzleInput)
solve2(puzzleInput)
print("------------------")
sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

width, height = 101, 103
midRow = height // 2
midCol = width // 2

def moveRobots(robots):
  newRobots = []

  for r in robots:
    npos, nvel = r
    nx, ny = npos
    nv1, nv2 = nvel

    nx = (nx + nv1) % width
    ny = (ny + nv2) % height

    newRobots.append(((nx, ny), nvel))

  return newRobots

def calculateSafetyFactor(robots):
  q1, q2, q3, q4 = 0, 0, 0, 0

  for r in robots:
    pos = r[0]
    x, y = pos
    if y < midRow and x < midCol:
      q1 += 1
    elif y > midRow and x < midCol:
      q3 += 1
    elif y < midRow and x > midCol:
      q2 += 1
    elif y > midRow and x > midCol:
      q4 += 1
  return q1 * q2 * q3 * q4

def printGrid(robots):
  grid = []
  for _ in range(height):
    grid.append(['.']*width)
  
  for r in robots:
    pos = r[0]
    x, y = pos
    grid[y][x] = '#'
  
  for row in grid:
    print(''.join(row))


def solve1(input):
  width, height = 101, 103
  seconds = 100
  midRow = height // 2
  midCol = width // 2

  q1, q2, q3, q4 = 0, 0, 0, 0

  grid = []
  for _ in range(height):
    grid.append([0]*width)

  for line in input:
    pos, vel = line.split(' ')
    x, y = [int(n) for n in pos[2:].split(',')]
    v1, v2 = [int(n) for n in vel[2:].split(',')]
    
    # print('p={0},{1} -> v={2},{3}'.format(x, y, v1, v2))
    # print('calculating position after {0} seconds'.format(seconds))
    # print()
    # grid[y][x] = '1'
    # for row in grid:
    #   print(row)
    # print()
    # grid[y][x] = '.'
    for _ in range(seconds):
      x = (x + v1) % width
      y = (y + v2) % height
    # print('{0}, {1}'.format(x, y))
    try:
      grid[y][x] += 1
      if y < midRow and x < midCol:
        q1 += 1
      elif y > midRow and x < midCol:
        q3 += 1
      elif y < midRow and x > midCol:
        q2 += 1
      elif y > midRow and x > midCol:
        q4 += 1
    except:
      print('BROKE ON: p={0},{1} -> v={2},{3}'.format(x, y, v1, v2))
      print()

  # print()
  # for row in grid:
  #   print(' '.join([str(n) if n > 0 else '.' for n in row]))
  result = q1 * q2 * q3 * q4
  print('Result 1: {0}'.format(result))

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve1(sampleInput)
print("------------------")
print("Puzzle")

robots = []
for line in puzzleInput:
  pos, vel = line.split(' ')
  x, y = [int(n) for n in pos[2:].split(',')]
  v1, v2 = [int(n) for n in vel[2:].split(',')]
  robots.append(((x, y), (v1, v2)))

# Not a great solution
# But got us to the correct frame
i = 0
while i < 10000000:
  robots = moveRobots(robots)
  sf = calculateSafetyFactor(robots)
  i += 1
  if sf <= 104618820:
    print(i, sf)
    printGrid(robots)
    input()

print("------------------")
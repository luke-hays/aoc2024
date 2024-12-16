import math
import heapq

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

def parseInput(inp):
  grid = []
  end = []
  start = []

  for i in range(len(inp)):
    line = inp[i]
    nl = []
    for j in range(len(inp[i])):
      nl.append(line[j])
      if line[j] == 'E': end = (i, j)
      if line[j] == 'S': start = (i, j)
    grid.append(nl)

  return (grid, start, end)

def getTmpDirAndScore(currDir, currScore, d):
  tmpScore = currScore
  tmpDir = currDir

  if currDir == '>': 
    if d == (0, 1):
      tmpScore += 1
    elif d == (1, 0):
      tmpScore += 1001
      tmpDir = 'V'
    elif d == (-1, 0):
      tmpScore += 1001
      tmpDir = '^'
    else:
      return None

  if currDir == '^':
    if d == (-1, 0):
      tmpScore += 1
    elif d == (0, 1):
      tmpScore += 1001
      tmpDir = '>'
    elif d == (0, -1):
      tmpScore += 1001
      tmpDir = '<'
    else:
      return None

  if currDir == 'V': 
    if d == (1, 0):
      tmpScore += 1
    elif d == (0, 1):
      tmpScore += 1001
      tmpDir = '>'
    elif d == (0, -1):
      tmpScore += 1001
      tmpDir = '<'
    else:
      return None

  if currDir == '<': 
    if d == (0, -1):
      tmpScore += 1
    elif d == (1, 0):
      tmpScore += 1001
      tmpDir = 'V'
    elif d == (-1, 0):
      tmpScore += 1001
      tmpDir = '^'
    else:
      return None

  return (tmpScore, tmpDir)

def findPath(grid, start, end):
  score = math.inf
  
  # Use a priority queue to prioritze low scores
  pq = []  
  bestScores = {}
  paths = {}

  heapq.heappush(pq, (0, (tuple(start), '>')))
  while len(pq) > 0:
    priority, state = heapq.heappop(pq)

    if priority > score: continue


    pos = state[0]
    currDir = state[1]
    x, y = pos

    if (pos == end):
      print('pq:', priority)
      score = min(score, priority)
      continue

    for d in directions:
      nx, ny = x + d[0], y + d[1]
      if grid[nx][ny] == '#': continue

      results = getTmpDirAndScore(currDir, priority, d)
      
      if not results: continue
      tmpScore, tmpDir = results
      if tmpScore > score: continue

      if (nx, ny, tmpDir) not in bestScores or tmpScore < bestScores[(nx, ny, tmpDir)]:
        bestScores[(nx, ny, tmpDir)] = tmpScore

    

        if (nx, ny) not in paths: paths[(nx, ny)] = set()
        paths[(nx, ny)].add((x, y, currDir))
        heapq.heappush(pq, (tmpScore, ((nx, ny), tmpDir)))
    
  return paths

def solve1(inp):
  grid, start, end = parseInput(inp)
  paths = findPath(grid, start, end)

  copyGrid = [[c for c in line] for line in grid]
  path = paths[end]

  while len(path) > 0:
    state = path.pop()
    x, y = state[0], state[1]
    path = paths[x, y]
    copyGrid[x][y] = 'O'

  for row in copyGrid:
    print(' '.join(row))
  return

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve1(sampleInput)
print("------------------")
# print("Puzzle")
# solve1(puzzleInput)
# print("------------------")

import math

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
      if line[j] == 'E': end = [i, j]
      if line[j] == 'S': start = [i, j]
    grid.append(nl)

  return (grid, start, end)

# Inspired based on FloodFill algorithm used in micromouse
def createFloodArray(grid, end):
  w, h = len(grid[0]), len(grid)
  floodArray = [[0 if grid[i][j] != '#' else '#' for j in range(w)] for i in range(h)]

  queue = [(end, 0)]
  visited = set()

  while len(queue) > 0:
    node = queue.pop(0)
    x, y = node[0]
    rank = node[1]

    floodArray[x][y] = rank
    visited.add((x, y))

    for d in directions:
      nx, ny = x + d[0], y + d[1]
      if grid[nx][ny] == '#' or (nx, ny) in visited: continue
      queue.append(([nx, ny], rank + 1))

  return floodArray

def findPaths(grid, start, end):
  score = math.inf

  def dfs(pos, visited, rank, newScore, currDir):
    nonlocal score
    x, y = pos

    if grid[x][y] == 0:
      score = min(score, newScore)
      print(score)
      return

    for d in directions:
      nx, ny = x + d[0], y + d[1]
      
      if grid[nx][ny] == '#' or (nx, ny) in visited: continue
      # if grid[nx][ny] >= grid[x][y]: continue

      newRank = grid[nx][ny]
      tmpScore = newScore
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
          continue
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
          continue
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
          continue
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
          continue
      
      if tmpScore >= 127452: continue

      # print(tmpScore)
      visited.add((nx, ny))
      dfs([nx, ny], visited, newRank, tmpScore, tmpDir)
      visited.remove((nx, ny))

  v = {tuple(start)}
  r = grid[start[0]][start[1]]
  s = 0
  curr = '>'

  dfs(start, v, r, s, curr)

  return None

def solve1(inp):
  grid, start, end = parseInput(inp)
  floodArray = createFloodArray(grid, end)
  findPaths(floodArray, start, end)
  # for r in floodArray:
  #   print('  '.join([f'{c: >2}' for c in r]))
  return

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve1(sampleInput)
print("------------------")
print("Puzzle")
solve1(puzzleInput)
print("------------------")

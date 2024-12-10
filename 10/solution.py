sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def solve(input):
  nums = [[int(n) for n in line] for line in input]
  moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  trailheads = {}
  paths = {}
  summits = set()

  for i, row in enumerate(nums):
    for j, n in enumerate(row):
      if n == 0: trailheads[(i, j)] = 0
      if n == 9: summits.add((i, j))
      paths[(i, j)] = []
      for move in moves:
        dx, dy = i-move[0], j-move[1]
        if  dx >= 0 and dx < len(nums) and \
            dy >= 0 and dy < len(row) and \
            nums[dx][dy] == (n + 1):
          paths[(i, j)].append((dx, dy))

  # Part 1
  def dfs(pt, visited=set()):
    if pt in summits: 
      visited.add(pt)
    else: 
      for path in paths[pt]:
        if path in visited: continue
        dfs(path, visited)
    return
  
  def dfs2(pt, visited=set()):
    if pt in summits: 
      visited.add(pt)
      return 1
    score = 0
    for path in paths[pt]:
      score += dfs2(path, visited)
    return score
  
  for th in trailheads.keys():
    score2 = 0
    for path in paths[th]:
      score2 += dfs2(path)
    trailheads[th] = score2

  print("Result:", sum(trailheads.values()))

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve(sampleInput)
print("------------------")
print("Puzzle")
solve(puzzleInput)
print("------------------")

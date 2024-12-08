sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def solve(input):
  grid = [[c for c in line] for line in input]
  antennas = {}
  antinodes = set()

  for row in range(len(grid)):
    for col in range(len(grid[row])):
      char = grid[row][col]
      if char != '.' and char != '#':
        if char not in antennas:
          antennas[char] = [(row, col)]
        else:
          antennas[char].append((row, col))

  for k, v in antennas.items():
    for antenna in v:
      x1, y1 = antenna

      for neighbor in v:
        if neighbor == antenna: continue

        x2, y2 = neighbor
        rise, run = x1-x2, y1-y2
        x3, y3 = x1+rise, y1+run
        
        if x3 >= 0 and x3 < len(grid) and y3 >= 0 and y3 < len(grid[0]): antinodes.add((x3, y3))

  print("Result 1: ", len(antinodes))

  antinodes = set()
  for k, v in antennas.items():
    for antenna in v:
      x1, y1 = antenna

      for neighbor in v:
        if neighbor == antenna: continue

        antinodes.add(neighbor)
        antinodes.add(antenna)

        x2, y2 = neighbor
        rise, run = x1-x2, y1-y2
        x3, y3 = x1+rise, y1+run
        
        while x3 >= 0 and x3 < len(grid) and y3 >= 0 and y3 < len(grid[0]): 
          antinodes.add((x3, y3))
          x3, y3 = x3+rise, y3+run

  print("Result 2: ", len(antinodes))
  
sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve(sampleInput)
print("------------------")
print("Puzzle")
solve(puzzleInput)
print("------------------")

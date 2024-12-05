import re

sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

directions = [
  (-1, -1),
  (-1, 0),
  (-1, 1),
  (0, -1),
  (0, 1),
  (1, -1),
  (1, 0),
  (1, 1)
]

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def printGrid(grid):
  for row in grid:
    print(row)

# DFS Solution
def findValidXmas(crossword, row, col, direction, prevLetter = None):
  letter = crossword[row][col]

  if letter == 'S' and prevLetter == 'A':
    return True

  (x, y) = direction
  r, c =  row + x, col + y

  if r < 0 or c < 0 or r >= len(crossword) or c >= len(crossword[row]): return False

  if letter == 'X' and prevLetter == None:
    return findValidXmas(crossword, r, c, direction, letter)
  elif letter == 'M' and crossword[r][c] == "A" and prevLetter == 'X':
    return findValidXmas(crossword, r, c, direction, letter)
  elif letter == 'A' and crossword[r][c] == "S" and prevLetter == 'M':
    return findValidXmas(crossword, r, c, direction, letter)

  return False

def findValidMas(crossword, row, col):
  if row <= 0 or col <= 0 or row >= len(crossword)-1 or col >= len(crossword[row])-1: return 0

  valid = 0

  ul = crossword[row-1][col-1]
  ur = crossword[row-1][col+1]
  dl = crossword[row+1][col-1]
  dr = crossword[row+1][col+1]

  if ul == 'M' and ur == 'M' and dl == 'S' and dr == 'S':
    valid += 1
  if ul == 'S' and ur == 'S' and dl == 'M' and dr == 'M':
    valid += 1
  if ul == 'M' and dl == 'M' and ur == 'S' and dr == 'S':
    valid += 1
  if ul == 'S' and dl == 'S' and ur == 'M' and dr == 'M':
    valid += 1

  return valid

def solve(input):
  result1 = 0
  result2 = 0

  crossword = [[letters for letters in line] for line in input]
  
  for row in range(len(crossword)):
    for col in range(len(crossword)):
      if crossword[row][col] == 'X':
        for direction in directions:
          if (findValidXmas(crossword, row, col, direction)):
            result1 += 1
      if crossword[row][col] == 'A':
        result2 += findValidMas(crossword, row, col)

  print("Result 1: ", result1)
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

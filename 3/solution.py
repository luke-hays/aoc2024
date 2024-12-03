import re

sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def solve(input):
  result1 = 0
  result2 = 0

  instructions = ''.join(input)
  matches = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', instructions)
  
  for match in matches:
    nums = re.findall(r'\d{1,3}', match.group())
    result1 += (int(nums[0]) * int(nums[1]))

  matches = re.finditer(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', instructions)
  processMultiplication = True

  for match in matches:
    if (match.group() == 'do()'):
      processMultiplication = True
    elif (match.group() == 'don\'t()'):
      processMultiplication = False
    elif processMultiplication:
      nums = re.findall(r'\d{1,3}', match.group())
      result2 += (int(nums[0]) * int(nums[1]))

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

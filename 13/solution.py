import re
import math
import sympy

# My own solution has issues with floating point arithemetic. Relying on a library to assist
# print('X1 = {0}, X2 = {1}, PX = {2}'.format(x1, x2, px))
# print('Y1 = {0}, Y2 = {1}, PY = {2}'.format(y1, y2, py))
# print()
# print('Solving System of Equations:')
# print('{0}a + {1}b = {2}'.format(x1, x2, px))
# print('{0}a + {1}b = {2}'.format(y1, y2, py))

# a = (py - ((y2 * px)/ x2)) / (y1 - ((y2 * x1) / x2))
# b = (px / x2) - ((x1 * a) / x2)

# if a == math.floor(a) and b == math.floor(b): 
#   result += (3*a + b)
# else:
#   print('X1 = {0}, X2 = {1}, PX = {2}'.format(x1, x2, px))
#   print('Y1 = {0}, Y2 = {1}, PY = {2}'.format(y1, y2, py))
#   print('a = {0}, b = {1}'.format(a, b))
#   print()

sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

# This is a little slow
def useSympy(x1, y1, x2, y2, px, py):
  a, b = sympy.symbols('a b')
  eq1 = sympy.Eq(x1*a + x2*b, px)
  eq2 = sympy.Eq(y1*a + y2*b, py)

  solution = sympy.solve((eq1, eq2), (a, b))

  if solution[a] == math.floor(solution[a]) and solution[b] == math.floor(solution[b]):
    return (3*solution[a] + solution[b])
  
  return 0

# Faster than lib
def useCramersRule(x1, y1, x2, y2, px, py):
  a = abs((px * y2 - py * x2) / (x1 * y2 - y1 * x2))
  b = abs((px * y1 - py * x1) / (x1 * y2 - y1 * x2))
  if a == math.floor(a) and b == math.floor(b):
    return (3 * a + b)
  return 0

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def solve(input):
  result = 0
  i = 0
  while i < len(input):
    x1, y1 = [int(n) for n in re.findall(r'\d+', input[i])]
    i+=1
    x2, y2 = [int(n) for n in re.findall(r'\d+', input[i])]    
    i+=1
    px, py = [int(n) for n in re.findall(r'\d+', input[i])]
    i+=2

    result += useCramersRule(x1, y1, x2, y2, px, py)

  print('Part 1 Result:', result)

  result = 0
  i = 0
  while i < len(input):
    x1, y1 = [int(n) for n in re.findall(r'\d+', input[i])]
    i+=1
    x2, y2 = [int(n) for n in re.findall(r'\d+', input[i])]    
    i+=1
    px, py = [10000000000000+int(n) for n in re.findall(r'\d+', input[i])]
    i+=2

    result += useCramersRule(x1, y1, x2, y2, px, py)

  print('Part 2 Result:', result)

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve(sampleInput)
print("------------------")
print("Puzzle")
solve(puzzleInput)
print("------------------")

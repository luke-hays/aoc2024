sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def verifyUpdateCorrectness(update, vertices):
  for j in range(len(update)-1):
    x, y = update[j], update[j+1]
    if y not in vertices[x]: return False
  return True

def solve(input):
  result1 = 0
  result2 = 0

  vertices = {}
  secondInstructionIndex = 0

  for i in range(len(input)):
    if input[i] == '':
      secondInstructionIndex = i+1
      break
    
    v, e = [int(x) for x in input[i].split('|')]

    if v not in vertices:
      vertices[v] = []
    if e not in vertices:
      vertices[e] = []

    vertices[v].append(e)

  for i in range(secondInstructionIndex, len(input)):
    update = [int(n) for n in input[i].split(',')]
    if verifyUpdateCorrectness(update, vertices):
      result1 += update[len(update)//2]
    else:
      n = len(update)
      for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
          if update[j] not in vertices[update[j+1]]:
            update[j], update[j+1] = update[j+1], update[j]
            swapped = True
        if (swapped == False):
          break
      result2 += update[len(update)//2]    

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

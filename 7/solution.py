sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def getCalibrationResult(val, nums, part2=False):
  def dfs(stack=[], i=0, addConcat=False):
    if i == len(nums):
      if (stack[-1] == val):
        return True
      return False

    if len(stack) == 0:
      stack.append(nums[0])
      return dfs(stack, 1, addConcat)

    result = stack[-1]
    newSum = result + nums[i]
    newProduct = result * nums[i]

    stack.append(newSum)
    sumPath = dfs(stack, i+1, addConcat)
    if sumPath: return True
    stack.pop()

    stack.append(newProduct)
    productPath = dfs(stack, i+1, addConcat)
    if productPath: return True
    stack.pop()

    if addConcat:
      newConcat = int(str(result) + str(nums[i]))
      stack.append(newConcat)
      concatPath = dfs(stack, i+1, addConcat)
      if concatPath: return True
      stack.pop()

    return False
  
  return val if dfs([], 0, part2) else 0

def solve(input):
  result1 = 0
  result2 = 0

  for line in input:
    testVal, numbers = line.split(': ')
    testVal = int(testVal)
    numbers = [int(n) for n in numbers.split(' ')]

    result1 += getCalibrationResult(testVal, numbers)
    result2 += getCalibrationResult(testVal, numbers, True)

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

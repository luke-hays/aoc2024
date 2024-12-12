sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def solve(input, blinks):
  total = 0
  memo = {}

  def blink(n):
    s = str(n)
    sLen = len(s)
    evenDigits = sLen % 2 == 0
    mid = sLen // 2

    # If the stone is 0 then this rock is just a 1
    if n == 0: return [1]
    # Otherwise we check the rule that if the number has an even amount of digits, we split it
    if evenDigits: return [int(s[:mid]), int(s[mid:])]
    return [n * 2024]

  def recursion(n, currDepth, maxDepth):
    if (currDepth, n) in memo: return memo[(currDepth, n)]
    if currDepth >= maxDepth: return 1

    stones = blink(n)
    currTotal = 0

    for stone in stones:
      currTotal += recursion(stone, currDepth+1, maxDepth)

    memo[(currDepth, n)] = currTotal

    return currTotal

  for n in [int(n) for n in input[0].split(' ')]:
    total += recursion(n, 0, blinks)

  return total

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
print('Part 1 Result:', solve(sampleInput, 25))
print('Part 2 Result:', solve(sampleInput, 75))
print("------------------")
print("Puzzle")
print('Part 1 Result:', solve(puzzleInput, 25))
print('Part 2 Result:', solve(puzzleInput, 75))
print("------------------")
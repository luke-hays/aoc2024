import heapq
import re

sample1 = "./sample1.txt"
sample2 = "./sample2.txt"
puzzle1 = "./puzzle1.txt"
puzzle2 = "./puzzle2.txt"

def readPuzzle(text):
  input = []

  with open(text) as file:
    input = [line.strip() for line in file]
  
  return input

def solve(input):
  list1 = []
  list2 = []

  heapq.heapify([])
  heapq.heapify([])

  for line in input:
    x, y = re.split(r'\s+', line)

    heapq.heappush(list1, int(x))
    heapq.heappush(list2, int(y))
  
  dist = 0
  while len(list1) > 0:
    dist += abs(heapq.heappop(list1) - heapq.heappop(list2))

  print("Result 1: ", dist)

  nums = []
  freq = {}
  for line in input:
    x, y = re.split(r'\s+', line)
    x, y = int(x), int(y)

    nums.append(int(x))
    if y not in freq:
      freq[y] = 1
    else:
      freq[y] += 1

  similarity = 0
  for n in nums:
    if n in freq:
      similarity += (n * freq[n])
  
  print("Result 2: ", similarity)
  print()

sample1Input = readPuzzle(sample1)
puzzle1Input = readPuzzle(puzzle1)

solve(sample1Input)
solve(puzzle1Input)
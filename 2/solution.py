import re

sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

class Report():
  levels = []
  
  def __init__(self, reportData):
    if type(reportData) is str:
      self.levels = re.split(r'\s+', reportData)
      self.levels = [int(x) for x in self.levels]
    else:
      self.levels = reportData

  def printData(self):
    print(self.levels)

  # Report is only safe if all levels are either increasing or decreasing
  # Any two adjacent levels differ by at least one and at most three
  def isReportSafe(self):
    def checkConstraints(increasing = False):
      for i in range(1, len(self.levels)):
        curr, prev = self.levels[i], self.levels[i-1]
        diff = abs(curr - prev)
        valid = curr > prev if increasing else curr < prev
        valid = valid and (diff >= 1 and diff <= 3)

        if not valid: return False
      return True
    return checkConstraints() or checkConstraints(True)
    
def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def solve(input):
  reports = [Report(r) for r in input]
  safeCount = 0
  safeCountWithDampener = 0
  for report in reports:
    if report.isReportSafe(): safeCount += 1
    # Brute Force Solution
    for i in range(len(report.levels)):
      tmpLevels = report.levels[0:i] + report.levels[i+1:]
      tmpReport = Report(tmpLevels)
      if tmpReport.isReportSafe():
        safeCountWithDampener += 1
        break

  print("Result 1: ", safeCount)
  print("Result 2: ", safeCountWithDampener)
  
sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve(sampleInput)
print("------------------")
print("Puzzle")
solve(puzzleInput)
print("------------------")

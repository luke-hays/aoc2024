sampleTextPath = './sample.txt'
puzzleTextPath = './puzzle.txt'

def readPuzzleInput(textPath):
  input = []
  with open(textPath) as file:
    input = [line.strip() for line in file]
  return input

def solve(input):
  nums = [int(x) for x in list(input[0])]
  fids = []
  
  files, currId = {}, 0
  for i in range(len(nums)):
    if i % 2 == 0: 
      files[currId] = nums[i]
      fids.append(currId)
      currId += 1
    else:
      fids.append(None)

  # print("File Ids - Block Size:\t", files)
  # print("File Ids - Map to Nums:\t", fids)
  print("Evaluating input...\n")
  
  currId -= 1
  checksum = 0
  ptr = 0
  remainingFiles = len(files)

  for i in range(len(nums)):
    if remainingFiles == 0:
      # print('-----------------')
      # print('THIS IS THE NEEDED CHECKSUM')
      # print('-----------------')
      # print()
      break

    fid = fids[i]

    if i % 2 == 0:
      # print("Encountered File ID:", fid, '\tSize:', files[fid])
      # print("Moving ptr", ptr, 'by', files[fid], 'places...')
      for _ in range(files[fid]):
        checksum += (ptr * fid)
        files[fid] -= 1
        if files[fid] == 0:
          remainingFiles -= 1
        ptr += 1
    else:
      # print("Encountered Empty Space Size:", nums[i])
      # print("Moving ptr", ptr, 'by', nums[i], 'places...')
      for _ in range(nums[i]):
        # print("Moving block for file id:", currId)
        files[currId] -= 1
        checksum += (ptr * currId)
        if files[currId] == 0:
          currId -= 1
          remainingFiles -= 1
          # print('Finished moving file. File ID:', currId, 'is next')
        ptr += 1
    
    # print()

  print('Final ptr position:', ptr)
  print("Checksum:", checksum)
  return

def solve2(input):
  nums = [int(x) for x in list(input[0])]
  fids = []
  space = []
  
  files, currId = {}, 0
  for i in range(len(nums)):
    if i % 2 == 0: 
      files[currId] = nums[i]
      fids.append(currId)
      space.append(None)
      currId += 1
    else:
      space.append(nums[i])
      fids.append(None)

  # print()
  # print("File Ids - Block Size:\t", files)
  # print("File Ids - Map to Nums:\t", fids)
  # print("Free Space Indices:", space)
  print("Evaluating Part 2 input...\n")

  currId -= 1
  checksum = 0
  ptr = 0
  ptr2 = 0
  # s = ''

  for i in range(len(nums)):
    fid = fids[i]
    ptr2 += nums[i]
    if i % 2 == 0:
    #   print("Encountered File ID:", fid, '\tSize:', files[fid])
    #   print("Moving ptr", ptr, 'by', files[fid], 'places...')

      for _ in range(files[fid]):
        # print('Updating Checksum using', ptr, '*', fid, 'to ->', checksum + (ptr * fid))
        checksum += (ptr * fid)
        s += str(fid)
        files[fid] -= 1
        ptr += 1
        # if files[fid] == 0:
        #   remainingFiles -= 1
        
    else:
      # print("Encountered Empty Space Size:", nums[i])
      # print("Determining what files can be moved into the space...")

      for tmpId in range(currId, -1, -1):
        if files[tmpId] == None or files[tmpId] == 0: continue
        neededSpace = files[tmpId]
        if neededSpace > space[i]: continue

        # print('File ID:', tmpId, 'needs space', neededSpace)
        # print('Space at', i, 'has free space:', space[i])
        # print('Moving block...')

        space[i] -= neededSpace
        for _ in range(neededSpace):
          files[tmpId] -= 1
          # print('Updating Checksum using', ptr, '*', tmpId, 'to ->', checksum + (ptr * tmpId))
          checksum += (ptr * tmpId)
          s += str(tmpId)
          ptr += 1
    ptr += (ptr2-ptr)
    # print()
  # print('Final ptr position:', ptr)
  print("Checksum:", checksum)
  # print(s)

sampleInput = readPuzzleInput(sampleTextPath)
puzzleInput = readPuzzleInput(puzzleTextPath)

print("------------------")
print("Sample")
solve(sampleInput)
solve2(sampleInput)
print("------------------")
print("Puzzle")
solve(puzzleInput)
solve2(puzzleInput)
print("------------------")

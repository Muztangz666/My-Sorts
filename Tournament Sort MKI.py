# Run time: ( O(log n) + O(n) ) * n = O(n log n) + O(n^2) = O(n^2)

def UpdateArray(ArrayToSort, LastIndex):
  if(LastIndex <= 0):
    return
  
  # Performs Tournament Sort.
  def TournamentSort(ArrayToSrot, LastIndex):
    if(len(ArrayToSort) == 1):
      return ArrayToSort[0]
    # List to hold winners, final size: ceiling(ArrayToSort.Length / 2).
    WinnersList = []
    for i in range(0, len(ArrayToSort), 2):
      if(i == LastIndex): # Only one element left, gets added by default.
        WinnersList.append(ArrayToSort[i])
        break
      elif(ArrayToSort[i] < ArrayToSort[i + 1]):
        WinnersList.append(ArrayToSort[i + 1])
      else:
        WinnersList.append(ArrayToSort[i])
      
      if((i + 1) == LastIndex):
        break
    NewLastIndex = len(WinnersList) - 1
    return TournamentSort(WinnersList, NewLastIndex)
  
  MaxVal = TournamentSort(ArrayToSort, LastIndex)
  # Gets index of MaxVal from ArrayToSort.
  MaxIndex = -1
  for i in range(0, len(ArrayToSort)):
    if(ArrayToSort[i] == MaxVal):
      MaxIndex = i
      break
  ArrayToSort[MaxIndex], ArrayToSort[LastIndex] = ArrayToSort[LastIndex]
  UpdateArray(ArrayToSort, LastIndex - 1)

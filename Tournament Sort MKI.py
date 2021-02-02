# Run time: ( O(log n) + O(n) ) * n = O(n log n) + O(n^2) = O(n^2)

def UpdateArray(ArrayToSort, LastIndex):
  if(LastIndex <= 0):
    return
  
  # Performs Tournament Sort.
  def TournamentSort(ArrayToSort, LastIndex):
    if(len(ArrayToSort) == 1):
      return ArrayToSort[0]
    # List to hold winners of each comparison.
    # Final size: ceiling(ArrayToSort.Length / 2).
    WinnersList = []

    # Adds the largest value of each comparison to WinnersList.
    # Run time: O(log n).
    for i in range(0, len(ArrayToSort), 2):
      if(i == LastIndex): # Only one element left, gets added by default.
        WinnersList.append(ArrayToSort[i])
        break
      # Performs comparison on two consecutive array elements
      # if there are two or more elements in ArrayToSort.
      elif(ArrayToSort[i] < ArrayToSort[i + 1]):
        WinnersList.append(ArrayToSort[i + 1])
      else:
        WinnersList.append(ArrayToSort[i])
      
      # Exits the loop if all elements have been checked.
      if((i + 1) == LastIndex):
        break

    # TournamentSort is called again until there is only one element
    # left in the array being passed-the largest value in the array.
    NewLastIndex = len(WinnersList) - 1
    return TournamentSort(WinnersList, NewLastIndex)
  # End TournamentSort().
  
  MaxVal = TournamentSort(ArrayToSort, LastIndex)
  # Gets index of MaxVal from ArrayToSort.
  # Run time: O(n).
  MaxIndex = -1
  for i in range(0, len(ArrayToSort)):
    if(ArrayToSort[i] == MaxVal):
      MaxIndex = i
      break

  # Moves the largest value to the end of the array.
  ArrayToSort[MaxIndex], ArrayToSort[LastIndex] = ArrayToSort[LastIndex], ArrayToSort[MaxIndex]
  UpdateArray(ArrayToSort, LastIndex - 1)
# End UpdateArray().

# Test case.
TestArray = [1, 16, 7, 14, 12, 5, 3, 4, 8, 2, 11, 15, 6, 9, 10, 13, 1, 7, 15]
UpdateArray(TestArray, len(TestArray) - 1)
print("Final Array:", TestArray)

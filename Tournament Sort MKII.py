# More efficient version of MKI that saves only the index of the largest
# array element instead of saving the largest value of each comparison.
#
# Run time: O(log n) * n = O(n log n)

def UpdateArray(ArrayToSort, LastIndex):
  if(LastIndex <= 0):
    return

  # Performs Tournament Sort.
  def TournamentSort(ArrayToSort):
    MaxIndex = 0

    # Final result of the for loop already has the location of the largest element
    # of the array, removing the need for the recursive call contained in MKI.
    # Instead of adding the winner of each comparison to a list, it is compared to
    # the element whose index is being stored in MaxIndex.
    # Run time: O(log n).
    for i in range(0, LastIndex + 1, 2):
      if(i == LastIndex): # Last element of the array.
        if(ArrayToSort[i] > ArrayToSort[MaxIndex]):
          MaxIndex = i
        break
      # Performs comparison on two consecutive array elements
      # if there are two or more elements in ArrayToSort.
      elif(ArrayToSort[i] < ArrayToSort[i + 1]):
        if(ArrayToSort[i + 1] > ArrayToSort[MaxIndex]):
          MaxIndex = i + 1
      else:
        if(ArrayToSort[i] > ArrayToSort[MaxIndex]):
          MaxIndex = i
      
      # Exits the loop if all elements have been checked.
      if((i + 1) == LastIndex):
        break
    return MaxIndex
  # End TournamentSort().

  # Moves the largest value to the end of the array.
  MaxValIndex = TournamentSort(ArrayToSort)
  ArrayToSort[MaxValIndex], ArrayToSort[LastIndex] = ArrayToSort[LastIndex], ArrayToSort[MaxValIndex]
  UpdateArray(ArrayToSort, LastIndex - 1)
# End UpdateArray().

# Test case.
TestArray = [1, 16, 7, 14, 12, 5, 3, 4, 8, 2, 11, 15, 6, 9, 10, 13, 1, 7, 15]
UpdateArray(TestArray, len(TestArray) - 1)
print("Final Array:", TestArray)

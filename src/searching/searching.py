# STRETCH: implement Linear Search	
# 
test = [3, 7, 22, 8, 4 ,1]			
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if arr[i] == target:
      print("target", target)
      print("found", i)
      return i
    else:
      print("target", target)
      print("not found")
  return -1   # not found

linear_search(test, 22)
# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

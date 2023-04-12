#The algorithm finds the number x in the sorted array or returns "not found"

def binari_search(arr,x):
  low = 0
  hight = len(arr) - 1
  mid = 0
  while low <= hight:
    mid = (low + hight) // 2
    if arr[mid] < x:
      low = mid + 1 
    elif arr[mid] > x:
      hight = mid -1
    else:
      return mid
  return "not found"

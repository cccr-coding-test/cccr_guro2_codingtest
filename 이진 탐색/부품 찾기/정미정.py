def binary_search(box, start, end, target):
    while start <= end:
      mid = (start+end)//2

      if box[mid] == target:
        return True
      elif box[mid] > target:
        end = mid-1
      else:
        start = mid+1
    return False

N = int(input())
box = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))
box.sort()

for i in range(M):
  result = binary_search(box, 0, len(box)-1, target[i])
  if result == False:
      print("no", end=' ')
  else:
      print("yes", end=' ')

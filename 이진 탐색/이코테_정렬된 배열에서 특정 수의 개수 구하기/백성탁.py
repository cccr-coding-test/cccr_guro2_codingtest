cnt=0
def binary_search(array, target, start, end):
  global cnt
  if start>end:
    return cnt
  middle=(start+end)//2
  if array[middle]==target:
    cnt+=1
    binary_search(array, target, middle+1, end)
    binary_search(array, target, start, middle-1)
  elif array[middle] < target:
    binary_search(array, target, middle+1, end)
  else:
    binary_search(array, target, start, middle-1)
  

N,x = map(int, input().split())
array=list(map(int, input().split()))

binary_search(array, x, 0, N-1)

if cnt==0:
  print("-1")
else:
  print(cnt)
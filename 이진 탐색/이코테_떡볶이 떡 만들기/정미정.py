import sys 

n, m = map(int, sys.stdin.readline().rstrip().split()) 
height = list(map(int, sys.stdin.readline().rstrip().split()))[:n] 

def binary_search(array, target, start, end): 
  result = 0 
  while start <= end: 
    mid = (start + end) // 2 total = 0 # 현재 절단기 위치에 따른 떡 길이의 총합 
    
    for i in array: 
      if i > mid: 
        total += i - mid # 떡 길이가 부족하면 절단기를 왼쪽으로 이동 
        
    if total < target: 
        end = mid - 1 # 떡 길이가 충분하다면 절단기를 오른쪽으로 이동 
    else: 
         start = mid + 1 
         result = mid 
          
   return result 

print(binary_search(height, m, 0, max(height)))


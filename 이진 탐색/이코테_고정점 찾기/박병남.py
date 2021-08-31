def solution(array, start, end):
    if start>end:
        return -1
    mid = (start+end)//2
    if array[mid]==mid:
        return mid
    elif array[mid] > mid:
        return solution(array,start,mid-1)
    else:
        return solution(array,mid+1,end)
    
n=int(input())
mylist=list(map(int,input().split()))
print(solution(mylist,0,n-1))

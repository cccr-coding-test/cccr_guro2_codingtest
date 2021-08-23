n = int(input())

def solution(n):
    n = str(n)
    n = list(map(int, n))
    
    half = len(n)//2
    
    half_1 = sum(n[:half])
    half_2 = sum(n[half:])
    
    if half_1 == half_2 :
        answer = "LUCKY"
    else:
        answer = "READY"
    
    return answer

solution(n)

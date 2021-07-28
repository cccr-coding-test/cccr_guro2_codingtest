from bisect import bisect_left

n=int(input())
n_list=list(map(int,input().split()))

m=int(input())
m_list=list(map(int,input().split()))

n_list.sort()

for m_var in m_list:
    n_var = n_list[bisect_left(n_list,m_var)]
    if n_var==m_var:
        print('yes', end=' ')
    else:
        print('no', end=' ')

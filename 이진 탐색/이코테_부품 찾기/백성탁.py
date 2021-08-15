N= int(input())
N_list = list(map(int,input().split()))

M= int(input())
M_list = list(map(int,input().split()))

for i in M_list:
    if i in N_list:
        print('yes', end=' ')
    else:
        print('no', end=' ')


#-------------------------------------------------------------


C = set(N_list) & set(M_list)

for i in M_list:
    if i not in C:
        print('no', end=' ')
    else:
        print('yes', end=' ')
        





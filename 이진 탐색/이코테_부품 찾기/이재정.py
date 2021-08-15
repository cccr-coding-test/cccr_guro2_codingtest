from collections import defaultdict

def find_table(data):
    if data == 1:
        return True
    else:
        return False

n = int(input())
num = set(map(int, input().split()))    

m = int(input())
client = list(map(int, input().split()))

table = defaultdict(int)

for i in num:
    table[i]=1

for i in client:
    if find_table(table[i]):
        print("yes", end=" ")
    else:
        print("no", end=" ")
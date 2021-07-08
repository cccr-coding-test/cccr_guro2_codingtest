a, b, c=map(int,input().split())
i=(a*a/(b*b+c*c))**0.5
print(int(i*b),int(i*c))
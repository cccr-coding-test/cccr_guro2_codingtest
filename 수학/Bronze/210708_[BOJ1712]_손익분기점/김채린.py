#a=고정비용 b=가변비용 c=노트북 가격
#판매비용>고정비용+가변비용

a, b, c=map(int,input().split())

if b>=c:
    print("-1")
else:
    print((a//(c-b))+1)

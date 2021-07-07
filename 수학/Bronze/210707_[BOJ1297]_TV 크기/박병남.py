d,w,h=map(int,input().split())
rate=(d*d/(w*w+h*h))**(0.5)
print(int(w*rate),int(h*rate))

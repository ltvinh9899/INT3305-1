import math

def prob(n,p):
    return ((1-p)**(n-1))*p

def infoMeasure(n,p):
    return -math.log(prob(n,p),2)

def sumProb(N,p):
    s = 0
    for n in range(1,N):
        s += prob(n,p)
    return s
'''
khi ta đưa giá trị p và N (VD: p=0.6 và N=1000) vào thì sumProb(N,p) luôn cho giá trị là 1 
'''

def approxEntropy(N,p):
    s = 0
    for n in range(1,N):
        s += prob(n,p)*infoMeasure(n,p)
    return s

'''
hàm approxEntropy(N,p) là tổng s của các tích prob(N,p) (xác xuất của phân bố geomectric) và 
inforMeasure(N,p) (lượng tin của của phân bố geometric). Vì vậy hàm trên là Entropy của phân bố geometric
thay p=0.5 và N = 1000 ta có kết của Entropy là 2
'''

# print(sumProb(1000,0.6))
# print(approxEntropy(1000,0.5))

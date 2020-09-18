import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n, r):
    return factorial(n)/(factorial(n-r+1)*factorial(n-1))

def prob(n,p,r):
    return combination(n, r)*(p **r)*(1 - p)**(n-r)

def infoMeasure(n,p,r):
    return -math.log(prob(n,p,r),2)

def sumProb(N,p,r):
    s = 0
    for n in range(1,N):
        s += prob(n,p,r)
    return s
'''
phần này vì chưa chắc nên em không để lại mô tả ạ
'''

def approxEntropy(N,p,r):
    s = 0
    for n in range(1,N):
        s += prob(n,p,r)*infoMeasure(n,p,r)
    return s

'''
hàm approxEntropy(N,p) là tổng s của các tích prob(N,p) (xác xuất của phân bố binomial) và 
inforMeasure(N,p) (lượng tin của của phân bố binomial). Vì vậy hàm trên là Entropy của phân bố binomial
thay p=0.5 và N = 10 ta có kết của Entropy là 2.07
'''

# print(sumProb(100,0.6,3))
# print(approxEntropy(10,0.5,3))

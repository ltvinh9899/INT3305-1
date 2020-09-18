import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def combination(n, N):
    return factorial(N)/(factorial(n)*factorial(N - n))

def prob(n,p,N):
    return combination(n, N)*(p ** n)*(1 - p)**(N - n)

def infoMeasure(n,p,N):
    return -math.log(prob(n,p,N),2)

def sumProb(N,p):
    s = 0
    for n in range(1,N):
        s += prob(n,p,N)
    return s
'''
khi ta đưa giá trị p và N (VD: p=0.6 và N=1000) vào thì sumProb(N,p) luôn cho giá trị là 1 
'''

def approxEntropy(N,p):
    s = 0
    for n in range(1,N):
        s += prob(n,p,N)*infoMeasure(n,p,N)
    return s

'''
hàm approxEntropy(N,p) là tổng s của các tích prob(N,p) (xác xuất của phân bố binomial) và 
inforMeasure(N,p) (lượng tin của của phân bố binomial). Vì vậy hàm trên là Entropy của phân bố binomial
thay p=0.5 và N = 10 ta có kết của Entropy là 2.7
'''

# print(sumProb(100,0.6))
# print(approxEntropy(10,0.5))

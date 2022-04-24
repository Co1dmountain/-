from decimal import Decimal
#import numpy as np
import random
def arcsinx(x):
     #x=float(x)
     #arcsin定义域为[-1,1]，大于1或者小于-1超出定义域
     if x>1 or x<-1:
         #print('错误，请输入-1到1间的数')
          return 0

     if x>=0 and x<=1:
          arcsinx=0
          n = 0
          #定义计算精度
          delta = 0.000000001
          #泰勒展开近似计算
          while (Decimal(factorial(2*n))*Decimal(x)**Decimal((2*n+1))/(4**Decimal(n)*Decimal(factorial(n))*Decimal(factorial(n))*Decimal((2*n+1))) >= delta):
                arcsinx += Decimal(factorial(2*n))*Decimal(x)**Decimal((2*n+1))/(4**Decimal(n)*Decimal(factorial(n))*Decimal(factorial(n))*Decimal((2*n+1)))
                n = n + 1
          return arcsinx
     if x>=-1 and x<0:
          arcsinx = 0
          n = 0
          #定义计算精度
          delta = 0.000000001
          x=-x
          #泰勒展开近似计算
          while (Decimal(factorial(2*n))*Decimal(x)**Decimal((2*n+1))/(4**Decimal(n)*Decimal(factorial(n))*Decimal(factorial(n))*Decimal((2*n+1))) >= delta):
                arcsinx += Decimal(factorial(2*n))*Decimal(x)**Decimal((2*n+1))/(4**Decimal(n)*Decimal(factorial(n))*Decimal(factorial(n))*Decimal((2*n+1)))
                n = n + 1
          arcsinx = -arcsinx
          return arcsinx

def factorial(m):    #阶乘
     if m == 0:
         return 1
     else:
         result = 1
         for i in range(2,m+1):
             result = result*i
         return result

def test(angle):
    myArcsinx = float(arcsinx(angle))
    systemArcsinx = np.arcsin(angle)

    minus =systemArcsinx-myArcsinx

    return minus


#for i in range(1, 100):
#    x = random.uniform(-1, 1)
#    ans = test(x)
#    flag = True
#    if ans > 0.001:
#        flag = False
#    print('input : %.5f' % x, "minus", '%.9f' % ans, flag)


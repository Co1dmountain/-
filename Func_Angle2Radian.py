# import math
# import random
from math import pi


# 角度转弧度函数
def angle2radian(angel):
    radian = angel * pi / 180
    return radian


'''
# 测试函数
def test(angle):
    my_angel2radian = angle2radian(angle)
    system_angel2radian = math.radians(angle)
    error = system_angel2radian - my_angel2radian
    return error


# 产生随机数测试函数的正确性
for i in range(1, 100):
    x = random.uniform(-10000, 10000)
    ans = test(x)
    flag = True
    if ans > 0.001:
        flag = False
    print('input : %.5f' % x, "误差", '%.9f' % ans, flag)
'''

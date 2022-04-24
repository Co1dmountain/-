from math import pi

def factorial(n):#求阶乘
	result = 1
	for i in range(1,n+1):
		result *= i
	return result

def cos(radian):
	#输入角度值，返回角度值对应的cos值,精度到50次为止
	#radian = x/180*pi#将角度转化为弧度值
	result = 1
	for j in range(1, 50):#计算50次幂函数
		if j%2 == 0:
			result += (radian**(2*j))/factorial(2*j)
		else:
			result -= (radian**(2*j))/factorial(2*j)
	return round(result,3)#返回百分位精度的结果

#print(cos(60))

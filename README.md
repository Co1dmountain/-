# 现代软件工程
## 总体设计
### 三角函数计算器总体设计

* 顶层模块
 * 角度弧度转换模块
   * `角度转弧度`模块
   * `弧度转角度`模块
 * 三角函数计算模块
   * `sin`函数
   * `cos`函数
   * `arcsin`函数
   * `arctan`函数
 * 界面显示模块
   * `用户输入`模块
   * `计算`模块
   * `结果输出`模块
 * 测试模块

## 详细设计
具体功能实现方法及具体数据结构

* 数据结构约束
  * 角度弧度值均采用`float`型数据，保留小数点后`9`位
* 三角函数计算算法
  * 具体实现:计算过程利用函数实现,函数名统一为`小写三角函数名`,如`sin、cos`,输入输出遵循数据结构约束,且函数输入为`弧度`
  * 待补充。。。。。。


## 三角函数计算模块文件命名规则
`Func_`加上各自对应的函数名称`首字母大写`,如`Func_Sin`

## 测试模块
* 测试模块不单独编写函数进行实现，而是采用在各函数内部进行测试的方式，通过在`循环内生成随机数`并各自计算 `编写的函数值`与`python提供的内置方法`所计算的函数值进行`减法运算`，通过事先确定的`阈值`与`差值`进行比较来确定编写的函数是否正确及可用。用户可通过在界面上输入`想要测试的值`并通过`test`按钮进行相关测试，测试结果将输出到界面上。

## 三角函数计算模块文件命名规则
* `Func_`加上各自对应的函数名称`首字母大写`,如`Func_Sin`


Angle2Radian
## 角度转弧度函数



# display branch
对应整个显示模块,使用PyQt进行开发

# Func_Arcsin

# arcsin函数计算模块
  * 使用泰勒级数展开逼近
  * 输入范围从-1到1
  * 精度范围为小数点后九位

# arcsin函数计算模块测试结果
![1648642562(1)](https://user-images.githubusercontent.com/101335052/160832294-d8a499d4-a182-4ad9-943d-8ef99f1b0ce7.png)




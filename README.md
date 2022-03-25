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


## display branch
对应整个显示模块,使用PyQt进行开发


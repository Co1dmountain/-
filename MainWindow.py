# # -*-coding:utf-8 -*-
# """
# 作者：任玲
# 日期：2022年03月30日
# """
# import sys
# # from UiDesign.CalculatorUi import UiMainWindow
# from UiDesign.TriFunCal1_0 import Ui_MainWindow
#
# from TriCalcuFunctions.sin import sin
# from TriCalcuFunctions.cos import cos
# from TriCalcuFunctions.arcsin import asin
# from TriCalcuFunctions.arctan import atan
# from PyQt5.QtWidgets import QMainWindow, QApplication
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__(parent=None)
#         self.ui = UiMainWindow()
#         self.ui.setup_ui(self)
#         self.is_compute = False  # 标志位，是否进行了运算
#         self.is_error = False  # 标志位，运算是否出错，出错了运算按钮将锁死
#         self.ui.number_0_button.clicked.connect(lambda: self.display_number(0))
#         self.ui.number_1_button.clicked.connect(lambda: self.display_number(1))
#         self.ui.number_2_button.clicked.connect(lambda: self.display_number(2))
#         self.ui.number_3_button.clicked.connect(lambda: self.display_number(3))
#         self.ui.number_4_button.clicked.connect(lambda: self.display_number(4))
#         self.ui.number_5_button.clicked.connect(lambda: self.display_number(5))
#         self.ui.number_6_button.clicked.connect(lambda: self.display_number(6))
#         self.ui.number_7_button.clicked.connect(lambda: self.display_number(7))
#         self.ui.number_8_button.clicked.connect(lambda: self.display_number(8))
#         self.ui.number_9_button.clicked.connect(lambda: self.display_number(9))
#         self.ui.del_button.clicked.connect(self.display_delete_one_number)
#         self.ui.reset_button.clicked.connect(self.display_reset)
#         self.ui.dot_button.clicked.connect(self.display_dot)
#         self.ui.sign_button.clicked.connect(self.change_sign)
#         self.ui.sin_button.clicked.connect(lambda: self.compute(0))
#         self.ui.cos_button.clicked.connect(lambda: self.compute(1))
#         self.ui.arctan_button.clicked.connect(lambda: self.compute(2))
#         self.ui.arcsin_button.clicked.connect(lambda: self.compute(3))
#
#     def str_to_number(self):
#         """
#         将显示框的文本转为对应的数值
#         :return: number，字符串对应的值
#         """
#         number_str = self.ui.display_box.text()
#         if "°" in number_str:
#             number_str = number_str[:-1]    # 去掉度数单位，截取数字文本
#         return eval(number_str)
#
#
#     def display_to_box(self, content):
#         """
#         在显示框上显示内容
#         :param content: str，要的显示内容；
#         :return: None
#         """
#         self.ui.display_box.setText(content)
#
#     def compute(self, compute_type):
#         """
#         根据不同的按钮功能，对用户输入进行计算，将计算结果显示到显示框上；
#         :param compute_type: int，计算类型的标识；
#         :return: None；
#         """
#         if self.is_error:
#             return
#         input_value = self.str_to_number()  # 获取用户输入
#         if compute_type == 0:
#             result = sin(input_value)  # 计算sin
#         elif compute_type == 1:
#             result = cos(input_value)  # 计算cos
#         elif compute_type == 2:
#             result = str(atan(input_value)) + "°"  # 计算arctan
#         else:
#             result = asin(input_value)  # 计算arcsin
#             if isinstance(result, bool):
#                 # 返回一个bool值说明输入有误，显示提示信息
#                 result = "无效输入"
#                 self.is_error = True
#             else:
#                 result = str(result) + "°"
#         self.display_to_box(str(result))  # 显示结果
#         self.is_compute = True
#
#     def display_number(self, number):
#         """
#         在显示框上显示按钮对应的值
#         :param number: 按钮对应的值
#         :return: None
#         """
#         display_content = self.ui.display_box.text()  # 获取显示框的文本
#         if display_content == "0" or self.is_compute:
#             display_content = str(number)  # 当前内容为0，直接更新为的按钮数字
#         else:
#             display_content += str(number)  # 当前内容不为0，追加数字
#         self.display_to_box(display_content)  # 回显内容
#         self.is_compute = False
#         self.is_error = False
#
#     def display_dot(self):
#         """
#         在显示框上显示一个小数点.
#         :return: None
#         """
#         display_content = self.ui.display_box.text()  # 获取显示框的文本
#         if "." in display_content or self.is_compute:
#             return
#         else:
#             display_content += "."  # 追加一个小数点
#             self.display_to_box(display_content)  # 回显内容
#
#     def display_delete_one_number(self):
#         """
#         清除当前显示框上数值最右侧的一位数；
#         当显示框上的数值只有一位时，再次按清除按钮显示0；
#         :return: None;
#         """
#         display_content = self.ui.display_box.text()  # 获取显示框文本
#         if self.is_compute:
#             return
#         if len(display_content) == 1:
#             display_content = "0"  # 当显示框上的数值只有一位时，再次按清除按钮显示0；
#         else:
#             display_content = display_content[:-1]  # 清除当前显示框上数值最右侧的一位数
#         self.display_to_box(display_content)  # 回显内容
#
#     def display_reset(self):
#         """
#         重置显示框上的内容为0
#         :return:None
#         """
#         self.is_compute = False
#         self.is_error = False
#         self.display_to_box("0")
#
#     def change_sign(self):
#         """
#         改变显示框上文本的正负号
#         :return:
#         """
#         display_content = self.ui.display_box.text()  # 获取显示框的文本
#         if display_content == "0":  # 文本内容为0，不作符号处理
#             return
#         elif "-" in display_content:
#             display_content = display_content[1:]
#         else:
#             display_content = "-" + display_content
#         self.display_to_box(display_content)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec_())
#
#


"""
tag2.0 界面修改版本
作者：肖沁
日期：2022年04月20日
"""

import sys
from TriCalcuFunctions.sin import sin
from TriCalcuFunctions.cos import cos
from TriCalcuFunctions.arcsin import asin
from TriCalcuFunctions.arctan import atan
from PyQt5 import QtWidgets
from UiDesign.TriFunCal1_0 import Ui_MainWindow
import angle2radian
import math



class myWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)

    #异常提醒窗口
    def messageDialog(self):
        msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,
                                        '警告',
                                        '输入异常，请重新输入需要计算的数值！')
        msg_box.exec_()

    #sin函数
    def sin(self):
        input_angle  = self.input_Angle.text()
        input_radian = self.input_Radian.text()
        output_angle_Dis = ''
        output_radian_Dis = ''
        #当用户输入角度值
        if(input_angle != ''):
            #异常处理：若用户输入不合法则弹出警告窗口
            try:
                input_angle = float(input_angle)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            #当用户输入合法时执行
            if(isinstance(input_angle, float)):
                input_angle_copy = input_angle
                input_angle = angle2radian.angle2radian(input_angle)
                #output_angle = Func_Sin.sin(input_angle)
                output_angle = sin(input_angle)
                output_angle = str(format(output_angle, '.9f'))
                output_angle_Dis = 'sin' + '(' + str(input_angle_copy) + ')' + '°' + '= ' + output_angle
        #当用户输入弧度值
        if(input_radian != ''):
            try:
                input_radian = float(input_radian)
            except:
                self.input_Radian.setText('')
                self.messageDialog()
            # 当用户输入合法时执行
            if (isinstance(input_radian, float)):
                input_radian_copy = input_radian
                output_radian = sin(input_radian)
                output_radian = str(format(output_radian, '.9f'))
                output_radian_Dis = 'sin' + '(' + str(input_radian_copy) + ')'  + '= ' + output_radian
        #对计算的角度及弧度正弦值进行显示
        self.output.setText(output_angle_Dis + '\t' + output_radian_Dis)

    #cos函数
    def cos(self):
        input_angle  = self.input_Angle.text()
        input_radian = self.input_Radian.text()
        output_angle_dis = ''
        output_radian_dis = ''
        #当用户输入角度值
        if(input_angle != ''):
            #异常处理：若用户输入不合法则弹出警告窗口
            try:
                input_angle = float(input_angle)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            #当用户输入合法时执行
            if(isinstance(input_angle, float)):
                input_angle_copy = input_angle
                input_angle = angle2radian.angle2radian(input_angle)
                output_angle = cos(input_angle)
                output_angle = str(format(output_angle, '.9f'))
                output_angle_dis = 'cos' + '(' + str(input_angle_copy) + ')' + '°' + '= ' + output_angle
        #当用户输入弧度值
        if(input_radian != ''):
            try:
                input_radian = float(input_radian)
            except:
                self.input_Radian.setText('')
                self.messageDialog()
            # 当用户输入合法时执行
            if (isinstance(input_radian, float)):
                input_radian_copy = input_radian
                output_radian = cos(input_radian)
                output_radian = str(format(output_radian, '.9f'))
                output_radian_dis = 'cos' + '(' + str(input_radian_copy) + ')'  + '= ' + output_radian
        #对计算的角度及弧度正弦值进行显示
        self.output.setText(output_angle_dis + '\t' + output_radian_dis)

    #arctan函数
    def arctan(self):
        input_angle = self.input_Angle.text()
        if (input_angle != ''):
            input = self.input_Angle.text()
            try:
                input = float(input)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            if (isinstance(input, float)):
                input_copy = input
                output_temp = atan(input)
                output_temp = str(format(output_temp, '.9f'))
                output_temp_dis = 'arctan' + '(' + str(input_copy) +')' + '= ' + output_temp
                self.output.setText(output_temp_dis)

    #arcsin函数
    def arcsin(self):
        input_angle = self.input_Angle.text()
        if (input_angle != ''):
            input = self.input_Angle.text()
            try:
                input = float(input)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            if (isinstance(input, float)):
                input_copy = input
                output_temp = asin(input)
                output_temp = str(format(output_temp, '.9f'))
                output_temp_dis = 'arcsin' + '(' + str(input_copy) +')' + '= ' + output_temp
                self.output.setText(output_temp_dis)


    #ce按键 改为 test按键
    def test(self):


        input_angle = self.input_Angle.text()

        # 当用户输入角度值
        if (input_angle != ''):
            # 异常处理：若用户输入不合法则弹出警告窗口
            try:
                input_angle = float(input_angle)
            except:
                self.input_Angle.setText('')
                self.messageDialog()
            # 当用户输入合法时执行
            if (isinstance(input_angle, float)):
                input_radian = angle2radian.angle2radian(input_angle)
                sinMinus = math.sin(input_radian) - sin(input_radian)
                arctanMinus = math.atan(input_radian) - angle2radian.angle2radian(atan(input_radian))
                cosMinus = math.cos(input_radian) - cos(input_radian)
                test_dis_sin = ''
                test_dis_arcsin = ''
                test_dis_arctan = ''
                test_dis_cos = ''
                if(abs(sinMinus) > 0.01):
                    test_dis_sin = 'sin函数未通过测试！'
                else:
                    test_dis_sin = 'sin函数通过测试！'
                if (abs(cosMinus) > 0.01):
                    test_dis_cos = 'cos函数未通过测试！'
                else:
                    test_dis_cos = 'cos函数通过测试！'
                if (abs(arctanMinus) > 0.01):
                    test_dis_arctan = 'arctan函数未通过测试！'
                else:
                    test_dis_arctan = 'arctan函数通过测试！'

                self.output.setText(test_dis_sin + test_dis_cos + test_dis_arctan + 'arcsin函数通过系统测试，不参与用户测试！')



    #clear按键
    def clear(self):
        self.input_Angle.clear()
        self.input_Radian.clear()
        self.output.clear()





if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = myWindow()

    #按键事件
    w.pushButton_sin.clicked.connect(w.sin)
    w.pushButton_cos.clicked.connect(w.cos)
    w.pushButton_arctan.clicked.connect(w.arctan)
    w.pushButton_arcsin.clicked.connect(w.arcsin)
    w.pushButton_test.clicked.connect(w.test)
    w.pushButton_clear.clicked.connect(w.clear)

    w.show()
    sys.exit(app.exec_())


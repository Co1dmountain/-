
#三角函数测试程序

import unittest
from TriCalcuFunctions.sin import sin
from TriCalcuFunctions.cos import cos
from TriCalcuFunctions.arcsin import asin
from TriCalcuFunctions.arctan import atan


class TestFunc(unittest.TestCase):         # 测试类

    def test_sin(self):                    # 测试sin函数,选取一些计算值与标准值进行比较
        self.assertEqual(0, sin(0))
        self.assertEqual(0.5, sin(30))
        self.assertEqual(0.707, sin(45))
        self.assertEqual(0.866, sin(60))
        self.assertEqual(1, sin(90))
        self.assertEqual(0.866, sin(120))
        self.assertEqual(0.574, sin(145))
        self.assertEqual(0, sin(180))
        self.assertEqual(-0.5, sin(210))
        self.assertEqual(-1, sin(270))
        self.assertEqual(0, sin(360))
        self.assertEqual(-0.5, sin(-30))
        self.assertEqual(-0.707, sin(-45))
        self.assertEqual(-0.866, sin(-60))
        self.assertEqual(-1, sin(-90))
        self.assertEqual(-0.866, sin(-120))
        self.assertEqual(-0.574, sin(-145))
        self.assertEqual(0, sin(-180))
        self.assertEqual(1, sin(-270))
        self.assertEqual(0, sin(-360))


    def test_cos(self):                    # 测试cos函数，选取一些计算值与标准值进行比较
        self.assertEqual(1, cos(0))
        self.assertEqual(0.866, cos(30))
        self.assertEqual(0.707, cos(45))
        self.assertEqual(0.5, cos(60))
        self.assertEqual(0, cos(90))
        self.assertEqual(-0.5, cos(120))
        self.assertEqual(-0.819, cos(145))
        self.assertEqual(-1, cos(180))
        self.assertEqual(-0.866, cos(210))
        self.assertEqual(0, cos(270))
        self.assertEqual(1, cos(360))
        self.assertEqual(0.866, cos(-30))
        self.assertEqual(0.707, cos(-45))
        self.assertEqual(0.5, cos(-60))
        self.assertEqual(0, cos(-90))
        self.assertEqual(-0.5, cos(-120))
        self.assertEqual(-0.819, cos(-145))
        self.assertEqual(-1, cos(-180))
        self.assertEqual(0, cos(-270))
        self.assertEqual(1, cos(-360))


    def test_arcsin(self):                 # 测试arcsin函数，选取一些计算值与标准值进行比较
        self.assertEqual(0, asin(0))
        self.assertEqual(5.7, asin(0.1))
        self.assertEqual(11.5, asin(0.2))
        self.assertEqual(17.5, asin(0.3))
        self.assertEqual(23.6, asin(0.4))
        self.assertEqual(30, asin(0.5))
        self.assertEqual(36.9, asin(0.6))
        self.assertEqual(45, asin(0.7071))
        self.assertEqual(60, asin(0.8660))
        self.assertEqual(64.2, asin(0.9))
        self.assertEqual(90, asin(1))
        self.assertEqual(-5.7, asin(-0.1))
        self.assertEqual(-11.5, asin(-0.2))
        self.assertEqual(-17.5, asin(-0.3))
        self.assertEqual(-23.6, asin(-0.4))
        self.assertEqual(-30, asin(-0.5))
        self.assertEqual(-36.9, asin(-0.6))
        self.assertEqual(-45, asin(-0.7071))
        self.assertEqual(-60, asin(-0.8660))
        self.assertEqual(-64.2, asin(-0.9))
        self.assertEqual(-90, asin(-1))

    def test_arctan(self):                 # 测试arctan函数，选取一些计算值与标准值进行比较
        self.assertEqual(0, atan(0))
        self.assertEqual(30, atan(0.5773))
        self.assertEqual(45, atan(1))
        self.assertEqual(60, atan(1.732))
        self.assertEqual(84.29, atan(10))
        self.assertEqual(89.43, atan(100))
        self.assertEqual(0, atan(0))
        self.assertEqual(-30, atan(-0.5773))
        self.assertEqual(-45, atan(-1))
        self.assertEqual(-60, atan(-1.732))
        self.assertEqual(-84.29, atan(-10))
        self.assertEqual(-89.43, atan(-100))



if __name__ == '__main__':
    unittest.main()

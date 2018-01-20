# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 有中文出现的情况，需要u'内容'

X = np.arange(1, 10)


def draw_1():
    Y = [1 for x in X]
    plt.plot(X, Y, label='O(1)')


def draw_logn():
    Y = [np.log2(n) for n in X]
    plt.plot(X, Y, label='O(log n)')


def draw_n():
    Y = X
    plt.plot(X, Y, label='O(n)')


def draw_nlogn():
    Y = [n * np.log2(n) for n in X]
    plt.plot(X, Y, label='O(n log n)')


def draw_n2():
    Y = [math.pow(n, 2) for n in X]
    plt.plot(X, Y, label='O(n^2)')


def draw_2n():
    Y = [math.pow(2, n) for n in X]
    plt.plot(X, Y, label='O(2^n)')


draw_1()
draw_logn()
draw_n()
draw_nlogn()
draw_n2()
draw_2n()
plt.legend()
plt.title(u'时间复杂度')
plt.show()

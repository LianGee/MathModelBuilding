#-------------------------------------------------------------------------------
# Name:        RBMTest
# Purpose:
#
# Author:      LianGee
#
# Created:     10/09/2016
# Copyright:   (c) LianGee 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-*-coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def getSum2(a, b):#返回平方误差
    #print a[0:]
    #print b[0:]
    #print '----------------'
    diff = a[0:] - b[0:]

    #print abs(diff)
    #print '----------------'
    return np.sum(abs(diff))

def getDiff():
    healthy = open('..\healthy.txt', 'r')
    unhealthy = open('..\unhealthy.txt', 'r')
    diff = []
    rs1 = np.zeros((1,16))
    rs2 = np.zeros((1,16))
    for i in range(9445):
        rs1[0:] = (healthy.readline().strip()).split()
        rs2[0:] = (unhealthy.readline().strip()).split()
        diff.append(getSum2(rs1[0:],rs2[0:]))
    ax = range(9445)
    max = 0

    #print diff
    plt.plot(ax, diff)
    plt.show()

getDiff()

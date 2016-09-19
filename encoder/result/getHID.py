#-------------------------------------------------------------------------------
# Name:        findGene
# Purpose:
#
# Author:      LianGee
#
# Created:     20/09/2016
# Copyright:   (c) LianGee 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-*-coding: utf-8 -*-

def getHID():
    f = open("multi_phenos.txt", 'r')
    data = [[]]*1000
    for i in range(1000):
        line = f.readline()
        data[i] = line.split()
    f.close()
    fileName = ''
    for i in range(10):
        fileName = 'H_'+str(i) + '.txt'
        f = open(fileName, 'w+')
        for j in range(999):
            f.write(str(data[j][i]) + ' ')
        f.close()

getHID()

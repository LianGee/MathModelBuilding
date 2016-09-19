#-------------------------------------------------------------------------------
# Name:        findGene
# Purpose:
#
# Author:      LianGee
#
# Created:     10/09/2016
# Copyright:   (c) LianGee 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-*-coding: utf-8 -*-

import os

def getRs():#返回位点名，与位点标号
    f = open("rs.txt", 'r')
    rs_dic = {}
    rs = f.readline().split()
    f.close()
    print len(rs)
    for i in range(len(rs)):
        rs_dic[rs[i]] = i;

    return rs_dic

'''
返回一个300*len的矩阵gene_rs
len表示第i个基因中，位点个数
gene_rs[i]表示第基因i+1中所有位点
'''
def getGene():
    files = os.listdir('./gene_info/')
    gene_rs = [[]]*300
    gene_num = 0
    for i in range(300):
        filePath = './gene_info/' + files[i]
        gene_num = (files[i].split('.')[0]).split('_')[1]#获取基因标号
        f = open(filePath, 'r')
        l = lambda rs:rs.strip()
        gene_rs[int(gene_num)-1]= map(l, f.readlines())

        f.close()
    return gene_rs


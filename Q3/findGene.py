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

'''
从rs.txt中读取位点名称，标号为0-9445
'''
def getRs():#返回位点名，与位点标号
    f = open("rs.txt", 'r')
    rs_dic = {}
    rs = f.readline().split()
    f.close()
    for i in range(len(rs)):
        rs_dic[rs[i]] = i;

    return rs_dic

'''
返回一个300*len的矩阵gene_rs
len表示第i个基因中，位点个数
gene_rs[i]表示第i+1基因中所有位点
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

'''
high_prob_rs表示高概率致病位点
返回1-300个基因中含有高致病位点个数
'''
def getGeneWithHighProbRS(high_prob_rs):
    gene_rs = getGene()
    gene_with_high_rs = [0]*300

    #print gene_rs[0]
    for i in range(300):
        for j in range(len(gene_rs[i])):
            gene_rs_set = set(gene_rs[i])
            interaction_len = len(high_prob_rs & gene_rs_set)
            if interaction_len is not 0:#如果两个set交集不为空
                gene_with_high_rs[i] = interaction_len

    return gene_with_high_rs


def main():
    high_prob_rs = ['rs2273298','rs12145450','rs364642','rs1802353'\
                    'rs7368252','rs2229579','rs12042240','rs12136961'\
                    'rs17361679','rs11249209','rs17401924','rs1152984'\
                    'rs1883567','rs2250358'
    ]
    gene_with_high_rs = getGeneWithHighProbRS(set(high_prob_rs))
    print gene_with_high_rs
    for i in range(300):
        if gene_with_high_rs[i] is not 0:
            print i, ' ',


if __name__ == '__main__':
    main()

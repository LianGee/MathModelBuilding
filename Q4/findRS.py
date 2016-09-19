#-------------------------------------------------------------------------------
# Name:        findRs
# Purpose:
#
# Author:      LianGee
#
# Created:     20/09/2016
# Copyright:   (c) LianGee 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#-*-coding: utf-8 -*-

import matplotlib.pyplot as plt
import os

def getMaxProb(filePath, HP):
    f = open(filePath, 'r')
    prob = {}
    for i in range(9445):#9445
        #print i
        line = f.readline().split()
        temp = line[0].split(':')[1]
        prob[temp] = float(line[2])

        #print line,prob
    sorted_prob = sorted(prob.iteritems(), key = lambda a:a[1],reverse = False)
    f.close()
    f = open('max_prob'+HP+'.txt', 'w+')
    lst_prob = []
    ax = []
    for i in range(len(sorted_prob)):
        if sorted_prob[i][1] != 0:
            lst_prob.append(sorted_prob[i][1])
            ax.append(float(sorted_prob[i][0][2:-1]))
            f.write(sorted_prob[i][0] + ' ' + str(sorted_prob[i][1]))
            f.write('\n')
    f.close()
    plt.scatter(ax,lst_prob)
    plt.annotate('local max', xy = (ax[-1], lst_prob[-1]), xytext = (3, 1.5), \
        arrowprops = dict(facecolor = 'black', shrink = 0.1))
    #plt.show()
    return sorted_prob



def main():
    files = os.listdir('results/')
    filePath = ''
    lst_prob = []*10
    for i in range(len(files)):
        filePath = 'results/'
        filePath += files[i]
        #print filePath
        sorted_prob = getMaxProb(filePath,str(i))
        lst_prob.append(sorted_prob[-100:])

    lst_rs = []*10
    rs = []
    print len(lst_prob)
    #print lst_prob
    for i in range(10):
        rs = []
        for j in range(100):
            rs.append(lst_prob[i][j][0])
        lst_rs.append(rs)

    set_a = set(lst_rs[3])
    #print set(lst_rs[0])
    for i in range(3):
        set_b = set(lst_rs[i])
        set_a = set_a & set_b
    print len(set_a), set_a
    #getMaxProb(file)


if __name__ == '__main__':
    main()






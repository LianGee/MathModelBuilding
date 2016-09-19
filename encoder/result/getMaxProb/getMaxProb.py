#-------------------------------------------------------------------------------
# Name:        getMaxProb
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

def getMaxProb():
    f = open('../result.txt', 'r')
    prob = {}
    for i in range(9445):#9445
        line = f.readline().split()
        temp = line[0].split(':')[1]
        prob[temp] = float(line[2])

        #print line,prob
    sorted_prob = sorted(prob.iteritems(), key = lambda a:a[1],reverse = False)
    f.close()
    f = open('max_prob.txt', 'w+')
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

    plt.show()



def main():
    getMaxProb()
    pass

if __name__ == '__main__':
    main()

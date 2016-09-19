#-------------------------------------------------------------------------------
# Name:        prob
# Purpose:
#
# Author:      LianGee
#
# Created:     20/09/2016
# Copyright:   (c) LianGee 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt

def main():
    f = open('max_prob.txt', 'r')
    rs = []
    prob = []

    for i in range(1647):
        line = (f.readline()).split()

        rs.append(line[0])
        prob.append(line[1])
    ax = range(len(rs))

    plt.plot(ax, prob)
    plt.show()


if __name__ == '__main__':
    main()

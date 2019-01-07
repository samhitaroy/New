import numpy as np
from matplotlib import pyplot as plt
import os
my_path = os.path.dirname(__file__)
#my_path = Desktop

#alpha = [2.5, 6, 4.5, 5.5]
alpha1 = (np.arange(2,3.5,0.5),np.arange(7.5,9,0.5),np.arange(4,5.5,0.5),np.arange(7,8.5,0.5))
range_tuple = ((20, 200),(50, 100),(50, 200),(100, 200))
line_color = ['r--','b-','g-.','k-','y-','m-']
alpha = []
for j in range(0,len(range_tuple)):
    p = []
    x1 = []
    c = []
    d = range_tuple[j]
    plt.figure(j)
    alpha = alpha1[j]
    for k in range(1, len(alpha)+1):
        p.append([])
        x1.append([])
        c.append([])
        for i in range(*d):
            x1[k-1].append(i)
            xmin = min(x1[k-1])
            p[k-1].append(alpha[k-1]*((xmin**alpha[k-1]))/(i**(alpha[k-1]+1)))
            c[k-1].append(1 - (xmin/i)**alpha[k-1])    
        plt.subplot(1,2,1)
        plt.plot(x1[0],p[k-1], line_color[k-1], label = str(alpha[k-1]))
        plt.xlabel('Packet size in bytes -->')
        plt.ylabel('f(x)-->')
        plt.title('Probability density function')
        plt.legend(loc = 'upper right')
        plt.ylim(0,0.15)
        plt.xlim(d[0],d[1])
        plt.grid(linestyle='-', linewidth='0.5', color='black')
        plt.subplot(1,2,2)
        plt.plot(x1[0],c[k-1], line_color[k-1], label = str(alpha[k-1]))
        plt.xlabel('Packet size in bytes -->')
        plt.ylabel('F(x)-->')
        plt.title('Cummulative distribution function')
        plt.legend(loc = 'upper left')
        plt.ylim(0,1)
        plt.xlim(d[0],d[1])
        plt.grid(linestyle='-', linewidth='0.5', color='black')
    plt.savefig((my_path + '/images/' + str(j) + '.png'))
##plt.subplot(2,2,4)
##plt.margins(x = 0.1,y = 0.45)
##plt.plot(x1[0], c[3], label = str(alpha[3]))
#plt.show()


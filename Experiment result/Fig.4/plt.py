# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import re
from sklearn.preprocessing import minmax_scale
from IPython.core.pylabtools import figsize
from matplotlib.ticker import MultipleLocator

def str_process(str):
    temp=re.split('[\[\],\n]',str)
    temp.remove('')
    temp.remove('')

    temp=[float(x) for x in temp]
    # print(list(reversed(temp))[20:50])
    temp=[(temp[i]+temp[i+1]+temp[i+2]+temp[i+3]+temp[i+4])/5 for i in range(len(temp)-5)]
    return list(reversed(temp))[15:50]

if __name__ == '__main__':
    font_legend = {'family': 'Arial',
                   'weight': 'normal',
                   'size': 15,
                   }
    font_label = {'family': 'Arial',
                  'weight': 'normal',
                  'size': 18,
                  }
    df = pd.read_excel('./data.xlsx')

    print(str_process(df[0][0]))

    figsize(5, 3)
    plt.figure()
    plt.plot(np.arange(0,350,10),str_process(df[0][0]), color='red', linewidth=2, linestyle=':', markersize=8, marker='^',
             label='Interval=0ms')
    # plt.plot(df['step'], df['accuracy youku'], color='black', linewidth=3, linestyle=':', markersize=10, marker='.',
    #          label='Youku:LSTM')
    # plt.plot(df['step'], df['accuracy amazon'], color='darkgreen', linewidth=3, linestyle=':', markersize=10,
    #          marker='+', label='Amazon:LSTM')
    plt.plot(np.arange(0,350,10),str_process(df[20][0]), color='royalblue', linewidth=2, linestyle=':', markersize=8,
             marker='x',c='', label='Interval=10ms')
    plt.plot(np.arange(0,350,10),str_process(df[50][0]), color='seagreen', linewidth=2, linestyle=':', markersize=8,
             marker='o', label='Interval=50ms')
    # plt.plot(df['step'], df['accuracy youku reverse'], color='springgreen', linewidth=3, linestyle=':', markersize=10,
    #          marker='|', label='Youku:R-LSTM')
    # plt.plot(df['step'], df['accuracy amazon reverse'], color='purple', linewidth=3, linestyle=':', markersize=10,
    #          marker='^', label='Amazon:R-LSTM')
    # plt.ylim(0.4, 1.05)
    plt.xlim(0, 340)
    plt.grid()
    plt.tick_params(labelsize=15)
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Arial') for label in labels]
    plt.xlabel('Time (ms)', font_label)
    plt.ylabel('Coverage Rate', font_label)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend( ncol=1, prop=font_legend)
    foo_fig = plt.gcf()  # 'get current figure'
    plt.tight_layout()
    foo_fig.savefig('./inter-cover.eps', format='eps', dpi=1000,bbox_inches='tight')
    plt.show()

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
	temp = re.split('[\[\],\n]', str)
	temp.remove('')
	temp.remove('')

	temp = [float(x) for x in temp]
	# print(list(reversed(temp))[20:50])
	# temp = [(temp[i] + temp[i + 1] + temp[i + 2] + temp[i + 3] + temp[i + 4]) / 5 for i in range(len(temp) - 5)]
	return list(reversed(temp))[0:num]


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

	figsize(5, 3)
	plt.figure()
	num = 35
	interval = 100/1000
	l = np.arange(0, num * interval, interval)

	# print(str_process(df[10][0]))
	plt.plot(l, str_process(df[10][0]), color='red', linewidth=2, linestyle=':', markersize=8, marker='^',
			 label='Interval=10ms')
	plt.plot(l, str_process(df[30][0]), color='royalblue', linewidth=2, linestyle=':', markersize=8,
			 marker='x', c='', label='Interval=30ms')
	plt.plot(l, str_process(df[50][0]), color='seagreen', linewidth=2, linestyle=':', markersize=8,
			 marker='o', label='Interval=50ms')
	plt.plot(l, str_process(df[70][0]), color='black', linewidth=2, linestyle=':', markersize=8,
			 marker='*', label='Interval=70ms')
	# plt.ylim(0.4, 1.05)
	plt.xlim(0, (num-1)*interval)
	plt.grid()
	plt.tick_params(labelsize=15)
	ax = plt.gca()
	ax.xaxis.set_major_locator(MultipleLocator(5 * interval))
	ax.yaxis.set_major_locator(MultipleLocator(0.2))
	labels = ax.get_xticklabels() + ax.get_yticklabels()
	[label.set_fontname('Arial') for label in labels]
	plt.xlabel('Time (s)', font_label)
	plt.ylabel('Coverage Rate', font_label)
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
	ax.legend(ncol=1, prop=font_legend)
	foo_fig = plt.gcf()  # 'get current figure'
	plt.tight_layout()
	foo_fig.savefig('./inter-cover.eps', format='eps', dpi=1000, bbox_inches='tight')
	plt.show()

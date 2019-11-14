# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import re
from sklearn.preprocessing import minmax_scale
from IPython.core.pylabtools import figsize
from matplotlib.ticker import MultipleLocator
import seaborn as sns


def process(str):
	return list(map(float, str.split(' ')))


def list_generator(mean, dis, number):  # 封装一下这个函数，用来后面生成数据
	return np.random.normal(mean, dis * dis, number)  # normal分布，输入的参数是均值、标准差以及生成的数量


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
	# sns.boxplot(x='interval',y='coverage',data=df,hue='Algorithm',color='blue',fliersize=1)
	# df_base.boxplot(showfliers=False,patch_artist = True, boxprops = {'color':'orangered','facecolor':'pink'})
	# df.boxplot(showfliers=False,patch_artist = True, boxprops = {'color':'b','facecolor':'pink'},grid=True)
	# sns.boxplot()
	plt.boxplot(df.values, showfliers=False, patch_artist=True, boxprops={'color': 'b', 'facecolor': 'lightsteelblue'},
				labels=np.around(np.arange(1, 2.1, 0.1), 1))

	plt.ylim(0.63, 1)
	plt.grid()
	plt.tick_params(labelsize=14)
	ax = plt.gca()
	# ax.xaxis.set_major_locator(MultipleLocator(0.1))
	ax.yaxis.set_major_locator(MultipleLocator(0.05))
	labels = ax.get_xticklabels() + ax.get_yticklabels()
	[label.set_fontname('Arial') for label in labels]
	plt.xlabel('Telemetry Interval/Label Interval', font_label)
	plt.ylabel('Coverage Rate', font_label)
	# label.set_horizontalalignment("right")
	# # box = ax.get_position()
	# # ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])

	plt.legend(prop=font_legend)
	foo_fig = plt.gcf()  # 'get current figure'
	plt.tight_layout()
	foo_fig.savefig('./telemetry.eps', format='eps', dpi=1000, bbox_inches='tight')
	plt.show()

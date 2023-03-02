#EITHER MAKE BACKGROUND TRANSPARENT
## DEFINE THE WIDTH OF COLUMNS / ROWS WITHOUT DIVISION

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib
#3_1_input_file
# what we want:
## first, make all the non-zero values 1
## second, arrange columns in descending sort manner
## third, transpose the matrix
## make a presence absence plot

df_inf = pd.read_csv("../result/3_2_input_file",sep="\t",header=0,index_col=0)
df_header = list(df_inf.columns)
df_index = list(df_inf.index)
df_inf=df_inf.astype(bool).astype(int)

sum_col = pd.DataFrame(df_inf.sum(axis=0))

sum_col = sum_col.sort_values(by=0, ascending=False)
sum_colT = sum_col.T
sorted_index = list(sum_col.index)

################# to INCLUDE IN 3_1 ##################
c = 0
d = []
e = [0]
for si in sorted_index:
	c=c+1
	vi = sum_col[0][si]
	d.append(vi)
	if (vi>=d[c-2]):
		next
	else:
		print(str(c)+"\t"+str(d[c-2]))
		e.append(c)
e.append(17349)
e_str = []
for each_e in e:
	e_str.append(str(each_e))
################# to INCLUDE IN 3_1, and MODIFY THE HEATMAP BIT ##################

y_axis = []
for each in s:
	print(str(each)+"\t"+str(s_dict[each]))


df_inf = df_inf.reindex(sum_colT.columns, axis=1) ### RE ORDER COLUMN
df_infT = df_inf.T

df_yaxis = []
for i in (0,len(df_header)):
	df_yaxis.append(i)
#print(df_index)
for i in range(0,3):
	print(type(df_index[i]))
	print(type(e_str[i]))
print(type(e_str))
ax = sns.heatmap(df_inf.T,xticklabels=df_index)

for item in ax.get_yticklabels():
	item.set_rotation(0)
	item.set_size(0)
for item in ax.get_xticklabels():
	item.set_rotation(90)
	item.set_size(2)
	item.set_horizontalalignment('right')

plt.savefig('py_plot_EggOG',dpi=1000)
plt.show()

# INITIAL file name = make_input.py
import pandas as pd
import numpy as np

df_3_1 = pd.read_csv("3_1_input_file_m",sep="\t",header=0,index_col=0)
df_3_1 = df_3_1.fillna("0")

species_ordered_list = []
with open("species_ordered_list_final_m",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		species_ordered_list.append(lines)

overlap_index_3_3 = []
with open("3_3_index_overlaps",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		for l in line:
			if (l != ""):
				overlap_index_3_3.append(l)

df_3_3 = pd.DataFrame(columns=overlap_index_3_3, index=species_ordered_list)
for i in overlap_index_3_3:
	for j in species_ordered_list:
		df_3_3[i][j] = df_3_1[i][j]
print(df_3_3)
df_3_3.to_csv('3_3_input_file_m',sep="\t")


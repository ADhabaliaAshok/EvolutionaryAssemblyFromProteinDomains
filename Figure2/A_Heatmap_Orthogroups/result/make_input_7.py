# Protein abundance Heatmap
# Orthogroups vs Species
# 6_2475OG_input_file
# species_ordered_list_final_m

import math
import pandas as pd

df_of = pd.read_csv("Orthogroups.tsv",sep="\t",header=0,index_col=0)	#download file from DatabaseFiles - link in README file#
df_of = df_of.fillna("0")
df_header = list(df_of.columns)
df_index = list(df_of.index)

species_ordered_list = []
with open("species_ordered_list_final_m",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		species_ordered_list.append(lines)

og_2322 = []
with open("6_2475OG_input_file",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		og_2322.append(lines.split("\t")[0])

dict_species = dict((k,"") for k in species_ordered_list)
for sp in df_header:
	v = sp.split("_")[0]+"_"+sp.split("_")[1]
	dict_species[v] = sp

df = pd.DataFrame(index = og_2322, columns = species_ordered_list)
df_log2 = pd.DataFrame(index = og_2322, columns = species_ordered_list)

for o in og_2322:
	for s in species_ordered_list:
		s_col = dict_species[s]
		prots = df_of[s_col][o]
		l = len(prots.split(", "))
		if (l == 1):
			if (prots == "0"):
				#print(s_col+"\t"+o+"\t"+prots)
				df[s][o] = 0
				df_log2[s][o] = 0
			else:
				df[s][o] = 1
				df_log2[s][o] = 1
		elif (l > 1):
			df[s][o] = l
			df_log2[s][o] = math.log2(l)
		else:
			df[s][o] = 0
			df_log2[s][o] = 0

dfT = df.T
dfT.to_csv(r'7_input_file')
dfT_log2 = df_log2.T
dfT_log2.to_csv(r'7_input_file_log2')

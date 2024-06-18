import pandas as pd
import numpy as np

#interpro2go
interpro = set()
with open("interpro2go",'r') as inf:
	linesafter7 = inf.readlines()[6:]
	for lines in linesafter7:
		lines = lines.strip("\n")
		line = lines.split(":")[1]
		interpro.add(line.split(" ")[0])
interpro_GOannotation = dict((k,set()) for k in interpro)
with open("interpro2go",'r') as inf:
	linesafter7 = inf.readlines()[6:]
	for lines in linesafter7:
		lines = lines.strip("\n")
		line_ipr = lines.split(":")[1].split(" ")[0]
		line_GO = lines.split("> GO:")[1].split(";")[0]
		interpro_GOannotation[line_ipr].add(line_GO)


#4_input_file
#species_numbered_list_final_m
df = pd.read_csv("4_input_file",sep="\t",header=0,index_col=0)
df_header = list(df.columns)
print(df["IPR008862"]["Picea_abies"])

df_sum_index = ['set1','set2','set3','set4','set5','set6','set7','set8','set9']
df_sum = pd.DataFrame(0,columns=df_header, index=df_sum_index)

species_num = dict()
with open("species_numbered_list_final_m",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		species_num[line[1]] = int(line[0])
set_dict = dict()
for i in range(1,6):
	set_dict[i] = "set1"
for i in range(6,12):
	set_dict[i] = "set2"
set_dict[12] = "set3"
set_dict[13] = "set4"
set_dict[14] = "set5"
set_dict[15] = "set6"
for i in range(16,19):
	set_dict[i] = "set7"
for i in range(19,24):
	set_dict[i] = "set8"
for i in range(24,38):
	set_dict[i] = "set9"

for s in species_num:
	snum = species_num[s]
	sset = set_dict[snum]
	for h in df_header:
		df_sum[h][sset] = df_sum[h][sset] + df[h][s]
#print(df_sum)
#print(df_sum.dtypes)


df_mean = pd.DataFrame(float(0),columns=df_header, index=df_sum_index)
for h in df_header:
	for sset1 in df_sum_index:
		if (sset1 == "set1"):
			df_mean[h][sset1] = float(df_sum[h][sset1])/float(5)
		elif (sset1 == "set2"):
			df_mean[h][sset1] = float(df_sum[h][sset1])/float(6)
		elif (sset1 == "set3"):
			df_mean[h][sset1] = float(df_sum[h][sset1])
		elif (sset1 == "set4"):
			df_mean[h][sset1] = float(df_sum[h][sset1])
		elif (sset1 == "set5"):
			df_mean[h][sset1] = float(df_sum[h][sset1])
		elif (sset1 == "set6"):
			df_mean[h][sset1] = float(df_sum[h][sset1])
		elif (sset1 == "set7"):
			df_mean[h][sset1] = float(df_sum[h][sset1])/float(3)
		elif (sset1 == "set8"):
			df_mean[h][sset1] = float(df_sum[h][sset1])/float(5)
		else:
			df_mean[h][sset1] = float(df_sum[h][sset1])/float(14)
#print(df_mean)
#print(df_mean.dtypes)

#fold change between lineage and LCA

df_sum_index_minus0 = list()
for i in range(1,len(df_sum_index)):
	df_sum_index_minus0.append(df_sum_index[i])

df1 = pd.DataFrame(float(0),columns=df_header,index=["df1"]) #Cyanobacteria-nLCA
#index10 = ["set1","set2","set3","set4","set5","set6","set7","set8","set9"]
#index11 = ["set2","set3","set4","set5","set6","set7","set8","set9"]
#n10=38-1
#n11=38-6
index10 = ["set2"]
index11 = ["set3","set4"]
n10 = 12-6
n11 = 14-12
for ipr in df_header:
	add10 = 0
	add11 = 0
	mean10 = float(0)
	mean11 = float(0)
	foldchange_diff = float(0)
	foldchange = float(0) #mean11/mean10
	for val10 in index10:
		add10 = add10 + df_sum[ipr][val10]
	for val11 in index11:
		add11 = add11 + df_sum[ipr][val11]
	mean10 = float(add10)/float(n10)
	mean11 = float(add11)/float(n11)
	if (mean10 == float(0)):
		foldchange = mean11/float(1)
	else:
		foldchange = mean11/mean10
		foldchange_diff = mean11 - mean10
#	df1[ipr]["df1"] = foldchange
	df1[ipr]["df1"] = foldchange_diff
fold_change_1 = []
top10_1 = []
top10_withIPR_1 = [] #
domain_trend_1 = [] #
domain_up_1 = 0
domain_down_1 = 0
domain_same_1 = 0
for h in df_header:
	fold_change_1.append(df1[h]["df1"])
for f in fold_change_1:
	if (f < float(1)):
		domain_down_1 = domain_down_1 + 1
	elif (f == float(1)):
		domain_same_1 = domain_same_1 + 1
	else:
		domain_up_1 = domain_up_1 + 1
tup_1 = zip(fold_change_1, range(len(fold_change_1)))
sorted_list_1 = sorted(tup_1, key=lambda v: v[0], reverse=True)
top10_1 = sorted_list_1[:10]
for sl in top10_1:
	add2l = []
	add2l.append(sl[0])
	add2l.append(df_header[sl[1]])
	top10_withIPR_1.append(add2l)
domain_trend_1.append(domain_up_1)
domain_trend_1.append(domain_same_1)
domain_trend_1.append(domain_down_1)

highest_fc_1 = sorted_list_1[0][0]
n_highest_1 = 0
for sl_1 in range(0,len(sorted_list_1)):
	if (sorted_list_1[sl_1][0]==highest_fc_1):
		n_highest_1 = n_highest_1 + 1
top_n_1 = sorted_list_1[:n_highest_1]
#print(fold_change_1)
print(top10_withIPR_1)
#print(df1)

df2 = pd.DataFrame(0,columns=df_header) #Chlorophyta-nLCA
df3 = pd.DataFrame(0,columns=df_header) #M+C-nLCA
df4 = pd.DataFrame(0,columns=df_header) #K-nLCA
df5 = pd.DataFrame(0,columns=df_header) #C-nLCA
df6 = pd.DataFrame(0,columns=df_header) #Zygnematophceae-nLCA




########################################################################
df_sum_index_minus0 = list()
for i in range(1,len(df_sum_index)):
	df_sum_index_minus0.append(df_sum_index[i])
df_foldchange_stepbystep = pd.DataFrame(float(0),columns=df_header, index=df_sum_index_minus0)
for sset1 in df_sum_index_minus0:
	for h in df_header:
		sset0 = "set" + str(int(sset1.split("set")[1])-1)
		if (df_mean[h][sset0] == float(0)):
			df_foldchange_stepbystep[h][sset1] = float(df_mean[h][sset1])/float(1)
		else:
			df_foldchange_stepbystep[h][sset1] = float(df_mean[h][sset1])/float(df_mean[h][sset0])

#df_step1 = df_mean.iloc[:1]
df_foldchange_fromstep1 = pd.DataFrame(float(0),columns=df_header, index=df_sum_index_minus0)
for sset1 in df_sum_index_minus0:
	for h in df_header:
		if (df_mean[h]["set1"] == float(0)):
			df_foldchange_fromstep1[h][sset1] = float(df_mean[h][sset1])/float(1)
		else:
			df_foldchange_fromstep1[h][sset1] = float(df_mean[h][sset1])/float(df_mean[h]["set1"])

#print(df_foldchange_stepbystep)
#print(df_foldchange_fromstep1)

figure3 = dict((k,list()) for k in df_sum_index_minus0)
for i in df_sum_index_minus0:
	fold_change = []
	top10 = []
	top10_withIPR = [] #
	domain_trend = [] #
	domain_up = 0
	domain_down = 0
	domain_same = 0
	for h in df_header:
		fold_change.append(df_foldchange_stepbystep[h][i])
	for f in fold_change:
		if (f < float(1.0)):
			domain_down = domain_down + 1
		elif (f == float(1.0)):
			domain_same = domain_same + 1
		else:
			domain_up = domain_up + 1
	tup = zip(fold_change, range(len(fold_change)))
	sorted_list = sorted(tup, key=lambda v: v[0], reverse=True)
	top10 = sorted_list[:10]
	for sl in top10:
		add2l = []
		add2l.append(sl[0])
		add2l.append(df_header[sl[1]])
		top10_withIPR.append(add2l)
	domain_trend.append(domain_up)
	domain_trend.append(domain_same)
	domain_trend.append(domain_down)
	figure3[i].append(domain_trend)
	figure3[i].append(top10_withIPR)

fout = open("final_figure3_output_4Jan2023",'w+')
for fig3 in figure3:
	print(fig3 + "\t" + str(figure3[fig3]))
	fout.write(fig3 + "\t" + str(figure3[fig3]) + "\n")
fout.close()

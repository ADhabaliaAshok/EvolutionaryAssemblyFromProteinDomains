import math
import pandas as pd

species_ordered_list = []
with open("species_ordered_list_final_m",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		species_ordered_list.append(lines)

df_inf = pd.read_csv("../../../Figure1_JandV/B_Approaches/result/3_3_input_file_m",sep="\t",header=0,index_col=0)
df_header = list(df_inf.columns)
df_index = list(df_inf.index)
df_inf=df_inf.astype(bool).astype(int)

sum_col = pd.DataFrame(df_inf.sum(axis=0))

sum_col = sum_col.sort_values(by=0, ascending=False)
sum_colT = sum_col.T
sorted_index = list(sum_col.index)
stress_OG = []

stress_OG = []
for each in sorted_index:
	eachnl = list(str(each))
	eachn = ""
	if (len(eachnl) == 1):
		eachn = "OG000000" + str(each)
	elif (len(eachnl) == 2):
		eachn = "OG00000" + str(each)
	elif (len(eachnl) == 3):
		eachn = "OG0000" + str(each)
	elif (len(eachnl) == 4):
		eachn = "OG000" + str(each)
	elif (len(eachnl) == 5):
		eachn = "OG00" + str(each)
	elif (len(eachnl) == 6):
		eachn = "OG0" + str(each)
	stress_OG.append(eachn)

stress_spprot = set()
with open("all_species_stress_og_fromOrthogroupstsv_37species",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[1] in stress_OG):
			stress_spprot.add(line[0])

ipr_set = set()
with open("database_proteindomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		makek = "SPECIES_"+line[0]+"_PROT_"+line[1]
		if (makek in stress_spprot):
			ipr_set.add(line[2])
sp_ipr_num = dict((k1, dict((k2,0) for k2 in ipr_set)) for k1 in species_ordered_list)
with open("database_proteindomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		makek = "SPECIES_"+line[0]+"_PROT_"+line[1]
		if (line[0] in species_ordered_list):
			#print(line[0])
			if (makek in stress_spprot):
			#if (line[0] in species_ordered_list):
				print(line[0])
				sp_ipr_num[line[0]][line[2]] = sp_ipr_num[line[0]][line[2]] + int(line[3])

f = open("4_input_file_3_3",'w+')
f2 = open("4_input_file_log2_3_3",'w+')

f.write("SPECIES\DOMAINS")
f2.write("SPECIES\DOMAINS")
for i in ipr_set:
	f.write(","+i)
	f2.write(","+i)
for s1 in species_ordered_list:
	f.write("\n"+s1)
	f2.write("\n"+s1)
	for s2 in ipr_set:
		v = sp_ipr_num[s1][s2]
		f.write(","+str(v))

		if (v>1):
			v2 = v
		elif (v==1):
			v2 = 2
		elif (v==0):
			v2 = 1
		v3 = math.log2(v2)
		f2.write(","+str(v3))
f.close()
f2.close()

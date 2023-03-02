import math
import pandas as pd
# 3_1_input_file
# all_species_stress_og_fromOrthogroupstsv

df_inf = pd.read_csv("../../../Figure1_JandV/B_Approaches/result/3_1_input_file_m",sep="\t",header=0,index_col=0)
df_header = list(df_inf.columns)
df_index = list(df_inf.index)
df_inf=df_inf.astype(bool).astype(int)

sum_col = pd.DataFrame(df_inf.sum(axis=0))

sum_col = sum_col.sort_values(by=0, ascending=False)
sum_colT = sum_col.T
sorted_index = list(sum_col.index)
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

species_ordered_list = []
with open("../../../Database/species_ordered_list_final_m",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		species_ordered_list.append(lines)

stress_spprot = set()
with open("../../../Database/all_species_all_og_fromOrthogroupstsv_37species",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[1] in stress_OG):
			stress_spprot.add(line[0])
stress_og_spprot = dict((k,set()) for k in stress_spprot)
with open("../../../Database/all_species_all_og_fromOrthogroupstsv_37species",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[1] in stress_OG):
			#print(line)
			spname = line[0].split("_PROT_")[0].split("SPECIES_")[1]
			if (spname in species_ordered_list):
				#prot = line[0].split("_PROT_")[1]
				stress_og_spprot[line[0]].add(line[1])
stress_og_spprot_uniqprot = dict((k,dict((k2,set()) for k2 in species_ordered_list)) for k in stress_OG)
with open("../../../Database/all_species_all_og_fromOrthogroupstsv_37species",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[1] in stress_OG):
			#print(line)
			spname = line[0].split("_PROT_")[0].split("SPECIES_")[1]
			if (spname in species_ordered_list):
				prot = line[0].split("_PROT_")[1]
				stress_og_spprot_uniqprot[line[1]][spname].add(prot)

stress_og_spprot_uniqipr = dict((k,dict((k2,set()) for k2 in species_ordered_list)) for k in stress_OG)
with open("../../../Database/database_proteindomains",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		makek = "SPECIES_" + line[0] + "_PROT_" + line[1]
		#print(makek) ## DE BUG
		if (makek in stress_spprot):
			#print(makek) ## DE BUG
			makeog = stress_og_spprot[makek]
			if (len(makeog) != 0):
				for each_mog in makeog:
					stress_og_spprot_uniqipr[each_mog][line[0]].add(line[2])

# MAKE final INPUT file ##########################################
df1 = pd.read_csv("5_input_file_uniqipr",sep="\t",header=0,index_col=0)
df2 = pd.read_csv("5_input_file_uniqprot",sep="\t",header=0,index_col=0)

# color: domains, size: proteins
og_list = list(df2)
f_out = open("5_final_input_file_PROT_DOM_1",'w+')
f_out.write("SPECIES,variable,UPROTEINS,UDOMAINS")
for o in og_list:
	for s in species_ordered_list:
		f_out.write("\n")
		f_out.write(s)
		f_out.write(",")
		f_out.write(o)
		f_out.write(",")
		up = df2[o][s]
		ip = df1[o][s]
		up_l2 = 1
		ip_l2 = 1

		if (up > 1):
			up_l2 = up
		if (up == 1):
			up_l2 = 2
		if (up == 0):
			up_l2 = 1

		if (ip > 1):
			ip_l2 = ip
		if (ip == 1):
			ip_l2 = 2
		if (ip == 0):
			ip_l2 = 1

#		print(str(up_l2)+"\t"+str(ip_l2))
		f_out.write(str(math.log2(up_l2)))
		f_out.write(",")
		f_out.write(str(ip))
f_out.close()

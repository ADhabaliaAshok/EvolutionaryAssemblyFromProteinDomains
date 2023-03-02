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
with open("species_ordered_list_final_m",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		species_ordered_list.append(lines)

stress_spprot = set()
with open("all_species_stress_og_fromOrthogroupstsv_37species",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[1] in stress_OG):
			stress_spprot.add(line[0])
stress_og_spprot = dict((k,set()) for k in stress_spprot)
with open("all_species_stress_og_fromOrthogroupstsv_37species",'r') as inf:	#download file from DatabaseFiles - link in README file#
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
with open("all_species_stress_og_fromOrthogroupstsv_37species",'r') as inf:	#download file from DatabaseFiles - link in README file#
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
with open("database_proteindomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
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

# MAKE intermediate input files  #################################
# SPECIES VS OG = PROT#
f = open("5_input_file_uniqprot",'w+')
f.write("SPECIES\STRESS_OG")
for each_sog in stress_OG:
	f.write("\t"+each_sog)
for k1 in species_ordered_list:
	f.write("\n"+k1)
	for k2 in stress_OG:
		v = str(len(stress_og_spprot_uniqprot[k2][k1]))
		f.write("\t"+v)
f.close()

#database_proteindomains: species protein domain number
#database_OG3_3_EmbryophyteLCAdomains: OG dom1,dom2,...
dict1_3_3og_uniqdom = dict((k,set()) for k in stress_OG)
with open("database_OG3_3_EmbryophyteLCAdomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		lines = lines.replace("{","")
		lines = lines.replace("}","")
		lines = lines.replace("'","")
		lines = lines.replace(", ",",")
		line = lines.split("\t")
		if (line[1] != "set()"):
			uniqdoms = line[1].split(",")
			for ud in uniqdoms:
				dict1_3_3og_uniqdom[line[0]].add(ud)

prot_doms_set = set()
with open("database_proteindomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		prot_doms_set.add(lines.split("\t")[2])
og_doms_set = set()
with open("database_OG3_3_EmbryophyteLCAdomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		lines = lines.replace("{","")
		lines = lines.replace("}","")
		lines = lines.replace("'","")
		lines = lines.replace(", ",",")
		line = lines.split("\t")
		if (line[1] != "set()"):
			uniqdoms = line[1].split(",")
			for ud in uniqdoms:
				og_doms_set.add(ud)

print(len(prot_doms_set))
print(len(og_doms_set))
dict2_sp_dom_presence = dict((k,dict((k2,0) for k2 in og_doms_set)) for k in species_ordered_list)
with open("database_proteindomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[2] in og_doms_set):
			dict2_sp_dom_presence[line[0]][line[2]] = 1
		else:
			dict2_sp_dom_presence[line[0]][line[2]] = 0

dict3_sp_og_domcompletion = dict((k1,dict((k2,set()) for k2 in stress_OG)) for k1 in species_ordered_list)
for eachog in dict1_3_3og_uniqdom.keys():
	myogdoms = dict1_3_3og_uniqdom[eachog]
	for eachsp in species_ordered_list:
		for mod in myogdoms:
			dict3_sp_og_domcompletion[eachsp][eachog].add(dict2_sp_dom_presence[eachsp][mod])

stress_og_spprot_uniqipr_1 = dict((k,dict((k2,set()) for k2 in species_ordered_list)) for k in stress_OG)
for eachog1 in stress_OG:
	for eachsp1 in species_ordered_list:
#		print(str(dict3_sp_og_domcompletion[eachsp1][eachog1])+"\t"+str(len(dict3_sp_og_domcompletion[eachsp1][eachog1])))
		if (0 in dict3_sp_og_domcompletion[eachsp1][eachog1]):
			stress_og_spprot_uniqipr_1[eachog1][eachsp1] = 0
#			print(eachsp1+"\t"+eachog1)
		else:
			stress_og_spprot_uniqipr_1[eachog1][eachsp1] = 1

# SPECIES VS OG = IPR#
f = open("5_input_file_uniqipr",'w+')
f.write("SPECIES\STRESS_OG")
for each_sog in stress_OG:
	f.write("\t"+each_sog)

for k1 in species_ordered_list:
	f.write("\n"+k1)
	for k2 in stress_OG:
		v = str(stress_og_spprot_uniqipr_1[k2][k1])
		f.write("\t"+v)
f.close()
############################################################

# load anaconda3@2020.11

import pandas as pd
import numpy as np


#MAKE LIST OF AtPp STRESS PROTEINS FROM PEATmoss & TAIR DATABASE
database_go = set()
with open("Ppatens_GO",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		if (lines != ""):
			line = lines.split(":")
			for each in line:
				database_go.add("GO:"+each)

with open("ATH_GO_GOSLIM_2021_removed4lines.txt",'r') as inf: #download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		database_go.add(lines.split("\t")[5])

database_stress_GO = set()
with open("PEATmossTAIR_GOBP_GORTS",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		database_stress_GO.add(lines)

database_stress_proteins_AtPp = set()
with open("PEATmossTAIR_stress_proteins",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		database_stress_proteins_AtPp.add(lines)

df_interproscan = pd.read_csv("concat_all_files_len13_ipr",sep="\t",header=0)	#download file from DatabaseFiles - link in README file#
df_interproscan.set_index("PROTEIN_NAME")

df_orthofinder = pd.read_csv("Orthogroups.tsv",sep="\t",header=0)	#download file from DatabaseFiles - link in README file#
df_orthofinder.set_index("Orthogroup") # this step is not working but it does not matter since it is unique with the inde number itself
df_orthofinder = df_orthofinder.fillna("0")

OG_lines_list = []
with open("Orthogroups.tsv",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		OG_lines_list.append(lines)
OG_index_list = []
for oglines in OG_lines_list:
		oglines = oglines.strip("\n")
		ogline = oglines.split("\t")
		AtProt = ogline[5]
		PpProt = ogline[29]
		AtProts = AtProt.split(", ")
		PpProts = PpProt.split(", ")
		AtPpProts = set()
		for eachat in AtProts:
			eachatm=eachat.split(".")[0]
			AtPpProts.add(eachatm)
		for eachpp in PpProts:
			AtPpProts.add(eachpp)
		myintersect = AtPpProts.intersection(database_stress_proteins_AtPp)
		if (len(myintersect) >= 1):
			OG_index_list.append(int(oglines.split("\t")[0].split("OG")[1]))

## NEXT: get the proteins for each species using the OG number from OG_index_list

species_ordered_list = []
with open("species_ordered_list_final_m",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		species_ordered_list.append(lines)
my_df = pd.DataFrame(columns=OG_index_list, index=species_ordered_list)

of_sp_list = list(df_orthofinder.columns)
for sp in range(1,len(of_sp_list)):
	spname = of_sp_list[sp].split("_")[0] + "_" + of_sp_list[sp].split("_")[1]
	for i in OG_index_list:
		if (df_orthofinder[of_sp_list[sp]][i] != "0"):
			sp_prots = df_orthofinder[of_sp_list[sp]][i].split(", ")
			my_df[i][spname] = len(sp_prots)
my_df = my_df.fillna(0)
my_df.to_csv('3_1_input_file_m',sep="\t")

# load anaconda3@2020.11

import pandas as pd
import numpy as np

egg_stress_proteins = set()
with open("database_GOID_GORTS",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		egg_spname_proteinID = "SPECIES_" + line[0] + "_PROT_" + line[1]
		egg_stress_proteins.add(egg_spname_proteinID)

species_orthofinder_list = []
with open("Orthogroups.tsv",'r') as inf:	#download file from DatabaseFiles - link in README file#
	line1 = inf.readlines()[0]
	line1 = line1.strip("\n")
	line = line1.split("\t")
	for l in range(1,len(line)):
		spname = line[l].split("_")[0] + "_" + line[l].split("_")[1]
		species_orthofinder_list.append(spname)

all_uniq_protein = set() # MADE without adding the species name. len(all_uniq_protein) = 1040570
all_uniq_spname_protein = set() # MADE with species name in front of protein id. len(all_uniq_spname_protein) = 1042316
with open("Orthogroups.tsv",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		for i in range(1,len(line)):
			spname = species_orthofinder_list[i-1]
			prots = line[i].split(", ")
			for each_p in prots:
				sp_prot = "SPECIES_" + spname + "_PROT_" + each_p
				all_uniq_spname_protein.add(sp_prot) # MADE with species name in front of protein id. len(all_uniq_spname_protein) = 1042316

spnameProteinID_ogID = dict((k,set()) for k in all_uniq_spname_protein)
with open("Orthogroups.tsv",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		ogID = line[0]
		for i in range(1,len(line)):
			spname = species_orthofinder_list[i-1]
			prots = line[i].split(", ")
			for each_p in prots:
				sp_prot = "SPECIES_" + spname + "_PROT_" + each_p
				spnameProteinID_ogID[sp_prot].add(ogID)

proteinIntersection = all_uniq_spname_protein.intersection(egg_stress_proteins)

EggStress_ogID = set()
for each_pi in proteinIntersection:
	og_id = spnameProteinID_ogID[each_pi]
	for a in og_id: # EACH protein maps to only one orthogroup ( from orthofinder ), but using "for each" loop since the og ID is stored in a set variable
		b = a.split("OG0")[1]
		EggStress_ogID.add(int(b))

df_orthofinder = pd.read_csv("Orthogroups.tsv",sep="\t",header=0)	#download file from DatabaseFiles - link in README file#
df_orthofinder.set_index("Orthogroup") # this step is not working but it does not matter since it is unique with the index number itself
df_orthofinder = df_orthofinder.fillna("0")

EggStress_ogID_list = list(EggStress_ogID)
species_ordered_list = []
with open("species_ordered_list_final_m",'r') as inf:	#download file from DatabaseFiles - link in README file#
        for lines in inf:
                lines = lines.strip("\n")
                species_ordered_list.append(lines)
my_df = pd.DataFrame(columns=EggStress_ogID_list, index=species_ordered_list)

of_sp_list = list(df_orthofinder.columns)
for sp in range(1,len(of_sp_list)):
        spname = of_sp_list[sp].split("_")[0] + "_" + of_sp_list[sp].split("_")[1]
        for i in EggStress_ogID_list:
                if (df_orthofinder[of_sp_list[sp]][i] != "0"):
                        sp_prots = df_orthofinder[of_sp_list[sp]][i].split(", ")
                        my_df[i][spname] = len(sp_prots)
my_df = my_df.fillna(0)
my_df.to_csv('3_2_input_file',sep="\t")

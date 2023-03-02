import math
import pandas as pd

#4_input_file_log2
stress_domains = set()
with open("../../Figure2_JandV/A_Heatmap_ProteinDomains/result/4_input_file_log2_3_3",'r') as inf:
	lines1 = inf.readlines()[0]
	lines1 = lines1.strip("\n")
	line1 = lines1.split("\t")
	for i in range(1,len(line1)):
		stress_domains.add(line1[i])

#database_proteindomains
species_list = []
with open("database_OG3_3_Orthogroups.tsv",'r') as inf:	#download file from DatabaseFiles - link in README file#
	lines1 = inf.readlines()[0]
	lines1 = lines1.strip("\n")
	line1 = lines1.split("\t")
	for l1 in line1:
		species_list.append(l1)
species_mod_list = []
with open("database_OG3_3_Orthogroups.tsv",'r') as inf:	#download file from DatabaseFiles - link in README file#
	lines1 = inf.readlines()[0]
	lines1 = lines1.strip("\n")
	line1 = lines1.split("\t")
	for l1 in line1:
		if (l1 != "Orthogroup"):
			species_mod_list.append(l1.split("_")[0] + "_" + l1.split("_")[1])
stress_og = set()
dict_species_proteins = dict((k,set()) for k in species_mod_list)
with open("database_OG3_3_Orthogroups.tsv",'r') as inf:	#download file from DatabaseFiles - link in README file#
	linesafter1 = inf.readlines()[1:]
	for lines in linesafter1:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if(line[0]!="Orthogroup"):
			stress_og.add(line[0])
			for i in range(1,len(line)):
				i_split = line[i].split(", ")
				for each_i in i_split:
					if (each_i != ""):
						dict_species_proteins[species_mod_list[i-1]].add(each_i)
dict_domains_species_proteins = dict((k1,dict((k2,set()) for k2 in species_mod_list)) for k1 in stress_domains)
with open("database_proteindomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[2] in stress_domains):
			if (line[1] in dict_species_proteins[line[0]]):
				dict_domains_species_proteins[line[2]][line[0]].add(line[1])

dict_species_proteins_ogs = dict((k1,dict((k2,set()) for k2 in dict_species_proteins[k1])) for k1 in species_mod_list)
with open("database_OG3_3_Orthogroups.tsv",'r') as inf:	#download file from DatabaseFiles - link in README file#
	linesafter1 = inf.readlines()[1:]
	for lines in linesafter1:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[0] != "Orthogroup"):
			for i in range(1,len(line)):
				i_split = line[i].split(", ")
				for each_i in i_split:
					if (each_i != ""):
						dict_species_proteins_ogs[species_mod_list[i-1]][each_i].add(line[0])

dict_domains_species_ogs = dict((k1,dict((k2,set()) for k2 in species_mod_list)) for k1 in stress_domains)
with open("database_proteindomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		if (line[1] in dict_species_proteins[line[0]]):
			ogs = dict_species_proteins_ogs[line[0]][line[1]]
			if (line[2] in stress_domains):
				for og in ogs:
					dict_domains_species_ogs[line[2]][line[0]].add(og)

#################
# MAKE INTERMEDIATE FILES #
#################
fout_prot = open("5_input_file_uniqprot_spvsipr",'w+')
fout_prot.write("SPECIES\IPR")
for i in stress_domains:
	fout_prot.write("\t"+i)
for s in species_mod_list:
	fout_prot.write("\n"+s)
	for i in stress_domains:
		fout_prot.write("\t" + str(len(dict_domains_species_proteins[i][s])))
fout_prot.close()

fout_og = open("5_input_file_uniqog_spvsipr",'w+')
fout_og.write("SPECIES\IPR")
for i in stress_domains:
	fout_og.write("\t"+i)
for s in species_mod_list:
	fout_og.write("\n"+s)
	for i in stress_domains:
		fout_og.write("\t" + str(len(dict_domains_species_ogs[i][s])))
fout_og.close()

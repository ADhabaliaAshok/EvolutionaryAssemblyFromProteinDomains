#database_AtPpprotannotations
#/usr/users/ashok/OrthologsProject/SpeciesDB/OF_run_remove_them_completely_from_this_dir/OrthoFinder/Results_Feb17/Orthogroups/Orthogroups.tsv
#3_3_index_overlaps

import pandas as pd

df_of = pd.read_csv("../../../Database/Orthogroups.tsv",sep="\t",header=0,index_col=0)
df_of = df_of.fillna(0)
dfT = df_of.T

index = set()
with open("../../../Figure1_JandV/B_Approaches/result/3_3_index_overlaps",'r') as inf:
	lines1 =  inf.readlines()[0]
	lines1 = lines1.strip("\n")
	line = lines1.split("\t")
	for l in line:
		addl = ""
		if (l != ""):
			if (len(l) == 1):
				addl = "OG000000" + l
			elif (len(l) == 2):
				addl = "OG00000" + l
			elif (len(l) == 3):
				addl = "OG0000" + l
			elif (len(l) == 4):
				addl = "OG000" + l
			elif (len(l) == 5):
				addl = "OG00" + l
			elif (len(l) == 6):
				addl = "OG0" + l
			else:
				addl = "OG" + l
			index.add(addl)

dict_prot_ann = dict()
with open("../../../Database/database_AtPpprotannotations",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		dict_prot_ann[line[0]] = line[1]

dict_index_ann = dict((k,set()) for k in index)
for i in index:
	atprots = ""
	ppprots = ""
	if (dfT[i]["Arabidopsis_thaliana_Araport11.protein.primaryTranscriptOnly_replaced_ast"] != 0):
		atprots = dfT[i]["Arabidopsis_thaliana_Araport11.protein.primaryTranscriptOnly_replaced_ast"]
	if (dfT[i]["Physcomitrella_patens_v3.3_proteome_replaced_ast"] != 0):
		ppprots = dfT[i]["Physcomitrella_patens_v3.3_proteome_replaced_ast"]
	atprot = atprots.split(", ")
	atprot_mod = []
	for atp in atprot:
		atprot_mod.append(atp.split(".")[0])
	ppprot = ppprots.split(", ")
	set_atprot = set(atprot_mod)
	set_ppprot = set(ppprot)
	ann_atprot = set_atprot.intersection(dict_prot_ann.keys())
	ann_ppprot = set_ppprot.intersection(dict_prot_ann.keys())
	for each in ann_atprot:
		at_ann = dict_prot_ann[each]
		at_anns = at_ann.split("; ")
		for ata in at_anns:
			dict_index_ann[i].add(ata)
	for each in ann_ppprot:
		pp_ann = dict_prot_ann[each]
		pp_anns = pp_ann.split("; ")
		for ppa in pp_anns:
			dict_index_ann[i].add(ppa)

fout = open("3_3_index_PEATmossTAIRannotations",'w+')
for each in index:
	fout.write(each+"\t"+str(dict_index_ann[each]))
	fout.write("\n")
fout.close()


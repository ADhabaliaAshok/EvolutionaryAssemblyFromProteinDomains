# /usr/users/ashok/OrthologsProject/SpeciesDB/OrthoFinder/Results_Apr30/Orthogroups/Orthogroups.tsv
sp_list = []
with open("Orthogroups.tsv",'r') as infile:	#download file from DatabaseFiles - link in README file#
	lines1 = infile.readlines()[0]
	line1 = lines1.split("\t")[1:]
	for each_sp in line1:
		sp_list.append(each_sp.split("_")[0]+"_"+each_sp.split("_")[1])

og_set = set()
with open("Orthogroups.tsv",'r') as infile:	#download file from DatabaseFiles - link in README file#
	lines_after1 = infile.readlines()[1:]
	for lines in lines_after1:
		lines = lines.strip("\n")
		og_set.add(lines.split("\t")[0])

og_dict_prot = dict((k1,dict((k2, set()) for k2 in og_set)) for k1 in sp_list)
with open("Orthogroups.tsv",'r') as infile:	#download file from DatabaseFiles - link in README file#
	lines_after1 = infile.readlines()[1:]
	for lines in lines_after1:
		lines = lines.strip("\n")
		sp_prot = lines.split("\t")[1:]
		for i in range(0,len(sp_prot)):
			each_prot = sp_prot[i].split(", ")
			for each_p in each_prot:
				og_dict_prot[sp_list[i]][lines.split("\t")[0]].add(each_p)
f_out = open("all_species_stress_og_fromOrthogroupstsv_37species",'w')
for species in og_dict_prot:
	for ogs in og_dict_prot[species]:
		if(og_dict_prot[species][ogs]=={''}):
			next
		else:
			proteins = og_dict_prot[species][ogs]
			for each_prot in proteins:
				if (each_prot!=""):
					f_out.write("SPECIES_" + species + "_PROT_" + each_prot + "\t" + ogs)
					f_out.write("\n")
	print(species)
f_out.close()

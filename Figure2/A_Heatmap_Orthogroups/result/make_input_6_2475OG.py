#database_OG3_3_uniquedomains
#database_domainfirstappearance
#species_numbered_list_final_m

dict_sp_num = dict()
dict_num_sp = dict()
with open("species_numbered_list_final_m",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		dict_sp_num[line[1]] = int(line[0])
		dict_num_sp[int(line[0])] = line[1]

dict_dom_num = dict()
with open("database_domainfirstappearance",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		dict_dom_num[line[0]] = int(line[2])

dict_OGf_num = dict()
with open("database_OGfirstappearance",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		dict_OGf_num[line[0]] = int(line[1])

set_OGs = set()
with open("database_OG3_3_uniquedomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		lines = lines.replace("{","")
		lines = lines.replace("}","")
		lines = lines.replace("'","")
		line = lines.split("\t")
		if (line[1] != "set()"):
			set_OGs.add(line[0])

dict_OG3_3_allnum = dict((k,[0,0,0]) for k in set_OGs)
dict_OG3_3_minmaxnumOGf = dict((k,list()) for k in set_OGs)
with open("database_OG3_3_uniquedomains",'r') as inf:	#download file from DatabaseFiles - link in README file#
	for lines in inf:
		lines = lines.strip("\n")
		lines = lines.replace("{","")
		lines = lines.replace("}","")
		lines = lines.replace("'","")
		line = lines.split("\t")
		if (line[1] != "set()"):
			nums = []
			lin = line[1].split(", ")
			for l in lin:
				nums.append(dict_dom_num[l])
			dict_OG3_3_allnum[line[0]] = nums ## least num
			dict_OG3_3_minmaxnumOGf[line[0]].append(min(nums))
			dict_OG3_3_minmaxnumOGf[line[0]].append(max(nums))
			dict_OG3_3_minmaxnumOGf[line[0]].append(dict_OGf_num[line[0]])

fout = open("6_2475OG_input_file",'w')
for key1 in dict_OG3_3_minmaxnumOGf:
	fout.write(key1+"\t"+str(dict_OG3_3_minmaxnumOGf[key1][0])+"\t"+str(dict_OG3_3_minmaxnumOGf[key1][1])+"\t"+str(dict_OG3_3_minmaxnumOGf[key1][2]))
	fout.write("\n")
fout.close()

# now annotate the orthogroups at 2 levels .. the regular annotation of At / Pp proteins . the response to stress mapping

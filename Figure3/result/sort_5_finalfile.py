#5_intermediate_input_file_log2PROT_log2OG_sortedPROT_1
sortedPROT = []
sortedOG = []
with open("5_intermediate_input_file_log2PROT_log2OG_sortedPROT_1",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		sortedPROT.append(lines)
with open("5_intermediate_input_file_log2PROT_log2OG_sortedOG_1",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		sortedOG.append(lines)

#5_final_input_file_log2PROT_OG_1
fout_sPROT = open("5_final_input_file_log2PROT_OG_sortPROT_2",'w+')
for sP in sortedPROT:
	with open("5_final_input_file_log2PROT_OG_1",'r') as inf:
		for lines in inf:
			lines = lines.strip("\n")
			line = lines.split(",")
			if (sP == line[1]):
				fout_sPROT.write(lines)
				fout_sPROT.write("\n")

fout_sOG = open("5_final_input_file_log2PROT_OG_sortOG_2",'w+')
for sO in sortedOG:
	with open("5_final_input_file_log2PROT_OG_1",'r') as inf:
		for lines in inf:
			lines = lines.strip("\n")
			line = lines.split(",")
			if (sO == line[1]):
				fout_sOG.write(lines)
				fout_sOG.write("\n")

fout_sPROT.close()
fout_sOG.close()

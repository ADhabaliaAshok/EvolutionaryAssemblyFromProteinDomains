#5_final_input_file_log2PROT_log2OG_1
k1 = set()
k2 = set()
with open("5_final_input_file_log2PROT_log2OG_1",'r') as inf:
	linesafter1 = inf.readlines()[1:]
	for lines in linesafter1:
		lines = lines.strip("\n")
		line = lines.split(",")
		k1.add(line[0])
		k2.add(line[1])
dict_sum1 = dict((key2,float(0)) for key2 in k2)
dict_sum2 = dict((key2,float(0)) for key2 in k2)
with open("5_final_input_file_log2PROT_log2OG_1",'r') as inf:
	linesafter1 = inf.readlines()[1:]
	for lines in linesafter1:
		lines = lines.strip("\n")
		line = lines.split(",")
		dict_sum1[line[1]] = dict_sum1[line[1]] + float(line[2])
		dict_sum2[line[1]] = dict_sum2[line[1]] + float(line[3])

sorted_dict_sum1 = sorted(dict_sum1.items(), key = lambda kv:(kv[1], kv[0]))
sorted_dict_sum1.reverse()
print(type(sorted_dict_sum1))
fout1 = open("5_intermediate_input_file_log2PROT_log2OG_sortedPROT_1",'w+')
for i in range(0,100):
	fout1.write(sorted_dict_sum1[i][0] + "\n")
fout1.close()

sorted_dict_sum2 = sorted(dict_sum2.items(), key = lambda kv:(kv[1], kv[0]))
sorted_dict_sum2.reverse()
fout2 = open("5_intermediate_input_file_log2PROT_log2OG_sortedOG_1",'w+')
for i in range(0,100):
	fout2.write(sorted_dict_sum2[i][0] + "\n")
fout2.close()

set1 = set()
with open("3_1_index_final_m",'r') as inf:
#with open("sorted_index_OG",'r') as inf:
#with open("3_1_index",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
#		line = int(lines.split("OG")[1])
#		set1.add(str(line))
		line = lines.split("\t")
		for l in line:
			if (l != ""):
				set1.add(l)

set2 = set()
with open("3_2_index",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		line = lines.split("\t")
		for l in line:
			if (l != ""):
				set2.add(l)

set_i = set1.intersection(set2)
fout = open("3_3_index_overlaps",'w+')
for each in set_i:
	fout.write("\t"+each)
fout.close()
print(len(set_i))

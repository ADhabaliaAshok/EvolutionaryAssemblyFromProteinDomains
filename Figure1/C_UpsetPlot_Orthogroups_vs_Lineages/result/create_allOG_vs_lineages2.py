fout = open("Orthogroup_OGall_realone_lineages_01.csv",'w+')
with open("Orthogroup_OGall_realone_lineages_presence_absence.csv",'r') as inf:
	line1 = inf.readlines()[0]
	line1 = line1.strip("\n")
	fout.write(line1)
	fout.write("\n")

with open("Orthogroup_OGall_realone_lineages_presence_absence.csv",'r') as inf:
	linesafter1 = inf.readlines()[1:]
	for lines in linesafter1:
		lines = lines.strip("\n")
		line = lines.split(",")
		newline = []
		newline.append(line[0])
		for l in range(1,len(line)):
			if (line[l] == "0"):
				newline.append(line[l])
			else:
				newline.append("1")
		newlines = ""
		newlines = ",".join(newline)
		fout.write(newlines)
		fout.write("\n")
fout.close()

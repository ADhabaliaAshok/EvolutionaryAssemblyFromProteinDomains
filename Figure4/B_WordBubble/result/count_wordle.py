words = set()
with open("6_annotation_96OG_1.out",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		ann = lines.split("\t")[1]
		ann = ann.replace("set(","")
		ann = ann.replace(")","")
		ann = ann.replace("'","")
		ann = ann.replace(", ",",")
		ann = ann.replace(" ","_")
		anns = ann.split(",")
		for a in anns:
			words.add(a)
words_d = dict((k,0) for k in words)
with open("6_annotation_96OG_1.out",'r') as inf:
	for lines in inf:
		lines = lines.strip("\n")
		ann = lines.split("\t")[1]
		ann = ann.replace("set(","")
		ann = ann.replace(")","")
		ann = ann.replace("'","")
		ann = ann.replace(", ",",")
		ann = ann.replace(" ","_")
		anns = ann.split(",")
		for a in anns:
			words_d[a] = words_d[a] + 1

fout = open("wordle_input_withcount.csv",'w+')
for w1 in words:
	fout.write(str(words_d[w1])+","+w1+"\n")
fout.close()

fout1 = open("wordle_input_words.txt",'w+')
for w11 in words:
	n11 = words_d[w11]
	for i in range(0,n11):
		fout1.write(w11 + "\n")
fout1.close()

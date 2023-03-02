import pandas as pd

fout = open("Orthogroups_OGall_realone_presence_absence.tsv",'w+')
with open("Orthogroups_all_realone.tsv",'r') as inf:
	lines1 = inf.readlines()[0]
	lines1 = lines1.strip("\n")
	fout.write(lines1+"\t")
	fout.write("\n")
with open("Orthogroups_all_realone.tsv",'r') as inf:
	linesafter1 = inf.readlines()[1:]
	for lines in linesafter1:
		lines = lines.strip("\n")
		line = lines.split("\t")
		fout.write(line[0]+"\t")
		for l in range(1,len(line)):
			if (line[l] == ""):
				fout.write("0\t")
			else:
				fout.write("1\t")
		fout.write("\n")
fout.close()
df_of = pd.read_csv("Orthogroups_OGall_realone_presence_absence.tsv",sep="\t",header=0)
df_of = df_of.set_index("Orthogroup")
df_of = df_of.fillna("0")
df_of = df_of.apply(pd.to_numeric)
print(df_of)
f_tra = [df_of["Spinacia_oleracea"], df_of["Arabidopsis_thaliana"], df_of["Arabidopsis_lyrata"], df_of["Brassica_rapa"], df_of["Medicago_truncatula"], df_of["Pisum_sativum"], df_of["Lotus_japonicus"], df_of["Oryza_sativa"], df_of["Brachypodium_distachyon"], df_of["Amborella_trichopoda"], df_of["Gnetum_montanum"], df_of["Picea_abies"], df_of["Azolla_filiculoides"], df_of["Selaginella_moellendorffii"]]
df_tra = pd.concat(f_tra).groupby(['Orthogroup']).sum().reset_index()
df_tra = df_tra.set_index("Orthogroup")

f_bry = [df_of["Physcomitrella_patens"], df_of["Sphagnum_fallax"], df_of["Marchantia_polymorpha"], df_of["Anthoceros_punctatus"], df_of["Anthoceros_agrestis"], df_of["Mesotaenium_endlicherianum"]]
df_bry = pd.concat(f_bry).groupby(['Orthogroup']).sum().reset_index()
df_bry = df_bry.set_index("Orthogroup")

f_sa = [df_of["Penium_margaritaceum"], df_of["Spirogloeae_muscicola"], df_of["Chara_braunii"], df_of["Klebsormidium_nitens"], df_of["Chlorokybus_atmophyticus"], df_of["Mesostigma_viride"]]
df_sa = pd.concat(f_sa).groupby(['Orthogroup']).sum().reset_index()
df_sa = df_sa.set_index("Orthogroup")

f_chl = [df_of["Micromonas_pusilla"], df_of["Ostreococcus_lucimarinus"], df_of["Ulva_mutabilis"], df_of["Chlamydomonas_reinhardtii"], df_of["Chlorella_variabilis"], df_of["Coccomyxa_subellipsoidea"]]
df_chl = pd.concat(f_chl).groupby(['Orthogroup']).sum().reset_index()
df_chl = df_chl.set_index("Orthogroup")

f_cya = [df_of["Nostoc_punctiforme"], df_of["Trichormus_azollae"], df_of["Fischerella_thermalis"], df_of["Gloeomargarita_lithophora"], df_of["Oscillatoria_acuminata"]]
df_cya = pd.concat(f_cya).groupby(['Orthogroup']).sum().reset_index()
df_cya = df_cya.set_index("Orthogroup")

result = pd.concat([df_tra, df_bry, df_sa, df_chl, df_cya], axis=1, join='inner')
result.to_csv("Orthogroup_OGall_realone_lineages_presence_absence.csv")

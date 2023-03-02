#Fischerella_thermalis_GORTSvsIPR_approach2.out
#/usr/users/ashok/OrthologsProject/eggnogmapper/

import pandas as pd
import matplotlib.pyplot as plt
from upsetplot import UpSet
from upsetplot import from_memberships

sp1 = pd.read_csv("Mesostigma_viride_GORTSvsIPR_approach2.out",sep="\t")
sp2 = pd.read_csv("Micromonas_pusilla_GORTSvsIPR_approach2.out",sep="\t")
sp3 = pd.read_csv("Gloeomargarita_lithophora_GORTSvsIPR_approach2.out",sep="\t")
sp4 = pd.read_csv("Amborella_trichopoda_GORTSvsIPR_approach2.out",sep="\t")
sp5 = pd.read_csv("Picea_abies_GORTSvsIPR_approach2.out",sep="\t")
sp6 = pd.read_csv("Coccomyxa_subellipsoidea_GORTSvsIPR_approach2.out",sep="\t")
sp7 = pd.read_csv("Anthoceros_punctatus_GORTSvsIPR_approach2.out",sep="\t")
sp8 = pd.read_csv("Physcomitrella_patens_GORTSvsIPR_approach2.out",sep="\t")
sp9 = pd.read_csv("Mesotaenium_endlicherianum_GORTSvsIPR_approach2.out",sep="\t")
sp10 = pd.read_csv("Ulva_mutabilis_GORTSvsIPR_approach2.out",sep="\t")
sp11 = pd.read_csv("Azolla_filiculoidesFeb12_GORTSvsIPR_approach2.out",sep="\t")
sp12 = pd.read_csv("Arabidopsis_thaliana_GORTSvsIPR_approach2.out",sep="\t")
sp13 = pd.read_csv("Penium_margaritaceum_GORTSvsIPR_approach2.out",sep="\t")
sp14 = pd.read_csv("Brassica_rapa_GORTSvsIPR_approach2.out",sep="\t")
sp15 = pd.read_csv("Oryza_sativa_GORTSvsIPR_approach2.out",sep="\t")
sp16 = pd.read_csv("Spirogloeae_muscicola_GORTSvsIPR_approach2.out",sep="\t")
sp17 = pd.read_csv("Arabidopsis_lyrata_GORTSvsIPR_approach2.out",sep="\t")
sp18 = pd.read_csv("Chlorokybus_atmophyticus_GORTSvsIPR_approach2.out",sep="\t")
sp19 = pd.read_csv("Chlorella_variabilis_GORTSvsIPR_approach2.out",sep="\t")
sp20 = pd.read_csv("Gnetum_montanum_GORTSvsIPR_approach2.out",sep="\t")
sp21 = pd.read_csv("Lotus_japonicus_GORTSvsIPR_approach2.out",sep="\t")
sp22 = pd.read_csv("Anthoceros_agrestis_GORTSvsIPR_approach2.out",sep="\t")
sp23 = pd.read_csv("Chlamydomonas_reinhardtii_GORTSvsIPR_approach2.out",sep="\t")
sp24 = pd.read_csv("Oscillatoria_acuminata_GORTSvsIPR_approach2.out",sep="\t")
sp25 = pd.read_csv("Chara_braunii_GORTSvsIPR_approach2.out",sep="\t")
sp26 = pd.read_csv("Sphagnum_fallax_GORTSvsIPR_approach2.out",sep="\t")
sp27 = pd.read_csv("Klebsomidium_nitens_GORTSvsIPR_approach2.out",sep="\t")
sp28 = pd.read_csv("Medicago_truncatula_GORTSvsIPR_approach2.out",sep="\t")
sp29 = pd.read_csv("Marchantia_polymorpha_GORTSvsIPR_approach2.out",sep="\t")
sp30 = pd.read_csv("Brachypodium_distachyon_GORTSvsIPR_approach2.out",sep="\t")
sp31 = pd.read_csv("Trichormus_azollae_GORTSvsIPR_approach2.out",sep="\t")
sp32 = pd.read_csv("Spinacia_oleracea_GORTSvsIPR_approach2.out",sep="\t")
sp33 = pd.read_csv("Nostoc_punctiforme_GORTSvsIPR_approach2.out",sep="\t")
sp34 = pd.read_csv("Ostreococcus_lucimarinus_GORTSvsIPR_approach2.out",sep="\t")
sp35 = pd.read_csv("Fischerella_thermalis_GORTSvsIPR_approach2.out",sep="\t")
sp36 = pd.read_csv("Pisum_sativum_GORTSvsIPR_approach2.out",sep="\t")
sp37 = pd.read_csv("Selaginella_moellendorffii_GORTSvsIPR_approach2.out",sep="\t")

sp1 = sp1.set_index('GORTS\IPR')
sp2 = sp2.set_index('GORTS\IPR')
sp3 = sp3.set_index('GORTS\IPR')
sp4 = sp4.set_index('GORTS\IPR')
sp5 = sp5.set_index('GORTS\IPR')
sp6 = sp6.set_index('GORTS\IPR')
sp7 = sp7.set_index('GORTS\IPR')
sp8 = sp8.set_index('GORTS\IPR')
sp9 = sp9.set_index('GORTS\IPR')
sp10 = sp10.set_index('GORTS\IPR')
sp11 = sp11.set_index('GORTS\IPR')
sp12 = sp12.set_index('GORTS\IPR')
sp13 = sp14.set_index('GORTS\IPR')
sp14 = sp15.set_index('GORTS\IPR')
sp15 = sp16.set_index('GORTS\IPR')
sp16 = sp17.set_index('GORTS\IPR')
sp17 = sp18.set_index('GORTS\IPR')
sp18 = sp20.set_index('GORTS\IPR')
sp19 = sp21.set_index('GORTS\IPR')
sp20 = sp22.set_index('GORTS\IPR')
sp21 = sp23.set_index('GORTS\IPR')
sp22 = sp24.set_index('GORTS\IPR')
sp23 = sp26.set_index('GORTS\IPR')
sp24 = sp27.set_index('GORTS\IPR')
sp25 = sp28.set_index('GORTS\IPR')
sp26 = sp29.set_index('GORTS\IPR')
sp27 = sp30.set_index('GORTS\IPR')
sp28 = sp31.set_index('GORTS\IPR')
sp29 = sp32.set_index('GORTS\IPR')
sp30 = sp33.set_index('GORTS\IPR')
sp31 = sp34.set_index('GORTS\IPR')
sp32 = sp35.set_index('GORTS\IPR')
sp33 = sp36.set_index('GORTS\IPR')
sp34 = sp37.set_index('GORTS\IPR')
sp35 = sp38.set_index('GORTS\IPR')
sp36 = sp39.set_index('GORTS\IPR')
sp47 = sp40.set_index('GORTS\IPR')

sp = sp1 + sp2 + sp3 + sp4 + sp5 + sp6 + sp7 + sp8 + sp9 + sp10 + sp11 + sp12 + sp13 + sp14 + sp15 + sp16 + sp17 + sp18 + sp19 + sp20 + sp21 + sp22 + sp23 + sp24 + sp25 + sp26 + sp27 + sp28 + sp29 + sp30 + sp31 + sp32 + sp33 + sp34 + sp35 + sp36 + sp37

sp_rownames = list(sp.index.values)
sp_colnames = list(sp.columns)

sp_memberships_set = dict((k,set()) for k in sp_colnames)

for sp_C in sp_colnames:
	for sp_R in sp_rownames:
		sp_val = sp[sp_C][sp_R]
		if (sp_val!=0):
			sp_memberships_set[sp_C].add(sp_R)

sp_memberships_list = dict((k,list(sp_memberships_set[k])) for k in sp_colnames)
sp_memberships = dict((k,",".join(sp_memberships_list[k])) for k in sp_colnames)
sp_membership_lists = [categories.split(",") for categories in sp_memberships.values()]
sps = from_memberships(sp_membership_lists)

UpSet(sps,subset_size='count',min_subset_size=20,show_counts=True).plot()
plt.show()

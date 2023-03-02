import pandas as pd
import matplotlib.pyplot as plt
from upsetplot import UpSet
from upsetplot import from_memberships

sp_t = pd.read_csv("../result/Orthogroup_OG3_3_lineages_01.csv")
sp_t = sp_t.set_index('Orthogroup')
sp = sp_t.transpose()

print(sp)

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

UpSet(sps,subset_size='count',min_subset_size=1,show_counts=True).plot()
plt.show()

Figure 2B

Github link: https://github.com/ADhabaliaAshok/EvolutionaryAssemblyFromProteinDomains/tree/main
Owncloud link: https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA

Figure 2B shows the top 10 protein domain bursts at every ascending node from the 9 lineages of 37 species


## Description of the data and file structure
Protein Domain bursts are retrieved from the file database_proteindomains. The protein domains were summed up and sorted for each lineage. This number was normalized as follows:
	number of domains in lineage/number of species in lineage
The top 10 were selected at every node between lineages. Since one lineage encompasses the next lineages at most nodes, the repeated protein domain bursts were not considered from one node to the next. However, in the figure we show that they are still part of the proteome for that lineage.

Simple command-lines were used on the terminal to get the result. The figure was made manually on Affinity Designer.


## Sharing/Access information
DatabaseFiles (Owncloud Link): https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA
Interpro2GO: this is a website which gives gene ontology annotation for interproscanner annotated protein domains: https://www.ebi.ac.uk/GOA/InterPro2GO

## Code/Software
Code part 1: python3 final_figure_3.py
	INPUT FILES REQUIRED:
		Interpro2go – downloaded from https://www.ebi.ac.uk/GOA/InterPro2GO
	OUTPUT FILES:
		final_figure3_output_4Jan2023

Software used: Affinity Desinger to design the evolutionary tree with protein domain bursts

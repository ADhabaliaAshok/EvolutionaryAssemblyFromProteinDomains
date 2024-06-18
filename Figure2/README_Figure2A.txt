Figure 2A

Github link: https://github.com/ADhabaliaAshok/EvolutionaryAssemblyFromProteinDomains/tree/main
Owncloud link: https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA

Figure 2A shows the weighted distribution of stress annotated proteome across the 37 species


## Description of the data and file structure
This figure is divided into two parts of stress annotated proteome:
	Stress annotated Orthogroups: shows the ditribution of the presence and prevelance of stress-annotated proteins across the 37 species
	Stress annotated protein domains: shows the distribution of the presence and prevelance of protein domains present within the stress-annotated orthogroups across the 37 species


## Sharing/Access information
DatabaseFiles (Owncloud Link): https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA
Model organisms
	A.thaliana database: https://www.arabidopsis.org/download/list?dir=GO_and_PO_Annotations%2FGene_Ontology_Annotations
	P.patens database: https://peatmoss.plantcode.cup.uni-freiburg.de/ppatens_db/downloads.php

The base input file needed is the Stress-annotated orthogroups from Figure 1C Approach 3, and interproscanner files.


## Code/Software
Code part 1: python3 make_input_6_2475OG.py
	INPUT FILES REQUIRED (all files can be downloaded from DatabaseFiles):
		species_numbered_list_final_m - input 37 species list
		database_domainfirstappearance – from python3 create_database_domainfirstappearance.py
		database_OGfirstappearance – from python3 create_database_Ogfirstappearance.py
		database_OG3_3_uniquedomains – from python3 create_database_OG3_3_uniquedomains.py
	OUTPUT FILES:
		6_2475OG_input_file

Code part 2.1: python3 make_input_7.py
	INPUT FILES REQUIRED:
		Orthogroups.tsv – from README_Figure1C Code part 1
		species_ordered_list_final_m - input 37 species list
		6_2475OG_input_file – from Code part 1
	OUTPUT FILES:
		7_input_file
		7_input_file_log2

Code part 2.2: Rscript final_m_heatmap_7.R
	INPUT FILES REQUIRED
		7_input_file_log2
	OUTPUT FILES
		7_output_file_log2_heatmap.pdf

Code part 3.1: python3 extract_stress_og_37.py
	INPUT FILES REQUIRED:
		Orthogroups.tsv – from README_Figure1C Code part 1
	OUTPUT:
		all_species_stress_og_fromOrthogroupstsv_37species

Code part 3.2: python3 make_input_4.py
	INPUT FILES REQUIRED:
		species_ordered_list_final_m - input 37 species list
		3_3_input_file_m – from README_Figure1C Code part 4
		all_species_stress_og_fromOrthogroupstsv_37species – from Code part 3.1
		database_proteindomains – from create_database_proteindomains.py
	OUTPUT:
		4_input_file_3_3
		4_input_file_log2_3_3


Figure 1C

Github link: https://github.com/ADhabaliaAshok/EvolutionaryAssemblyFromProteinDomains/tree/main
Owncloud link: https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA

Figure 1C shows a comparison among three approaches to annotate proteins and orthologs as stress-relevant


## Description of the data and file structure
This figure is divided into three approaches of annotating proteins and orthologs with:
Approach 1: A.thaliana and P.patens model organisms open source database
Approach 2: Gene Ontology open source tool known as Eggnogmapper
Approach 3: Intersection of Approach 1 and Approach 2


## Sharing/Access information
DatabaseFiles (Owncloud Link): https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA
Model organisms
	1) A.thaliana database: https://www.arabidopsis.org/download/list?dir=GO_and_PO_Annotations%2FGene_Ontology_Annotations
	2) P.patens database: https://peatmoss.plantcode.cup.uni-freiburg.de/ppatens_db/downloads.php

The base input file needed is the 37 species clustered into orthogroups – obtained from Code part 1. The Orthogroups file is used to annotate the orthogroups and proteins as follows:
Approach 1 – from model organisms database, and orthogroup file
Approach 2 – fasta files of 37 species as input for Eggnogmapper, and orthogroup file
Approach 3 – orthogroup IDs from Approach 1 and Approach 2


## Code/Software
Code part 1: Create orthogroups using OrthoFinder
orthofinder.py -f /directory_with_37species_fasta_files/

Code part 2.1: python3 make_input_3_1.py
	INPUT FILES REQUIRED (all files can be downloaded from DatabaseFiles):
		Ppatens_GO - download file from P.patens database
		ATH_GO_GOSLIM_2021_removed4lines.txt – modified file from A.thaliana
		PEATmossTAIR_GOBP_GORTS - download file from P.patens database
		PEATmossTAIR_stress_proteins – modified from Ppatens_GO
		concat_all_files_len13_ipr – interproscanner files
		Orthogroups.tsv - from Code part 1
		species_ordered_list_final_m – input 37 species list
	OUTPUT FILES:
		3_1_input_file_m

Code part 2.2: python3 make_output_3_1.py
	INPUT FILES REQUIRED:
		3_1_input_file_m
	OUTPUT FILES:
		py_plot_AtPpOG_m.png – distribution of stress-annotated orthogroups from Approach 1

Code part 3.1: python3 make_input_3_2.py
	INPUT FILES REQUIRED (all files can be downloaded from DatabaseFiles):
		database_GOID_GORTS – output from python3 create_database_GO_GORTS.py
		Orthogroups.tsv – from Code part 1
		species_ordered_list_final_m - input 37 species list
	OUTPUT FILES:
		3_2_input_file

Code part 3.2: python3 make_output_3_2.py
	INPUT FILES REQUIRED:
		3_2_input_file
	OUTPUT FILES:
		py_plot_EggOG.png - distribution of stress-annotated orthogroups from Approach 2

Code part 4.1: python3 compare_index.py
	INPUT FILES REQUIRED:
		3_1_index_final_m - obtained from header of 3_1_input_file_m
		3_2_index - obtained from header of 3_2_input_file
	OUTPUT FILES:
		3_3_index_overlaps

Code part 4.2: python3 make_input_3_3.py
	INPUT FILES REQUIRED:
		3_1_input_file_m – from Code part 2
		species_ordered_list_final_m - input 37 species list
		3_3_index_overlaps – from Code part 4.1
	OUTPUT FILES:
		3_3_input_file_m

Code part 4.3: python3 make_output_3_3.py
	INPUT FILES REQUIRED:
		3_3_input_file_m
	OUTPUT FILES:
		py_plot_AtPpOG_EggOG_m.png - distribution of stress-annotated orthogroups from Approach 3


Figure 3A

Github link: https://github.com/ADhabaliaAshok/EvolutionaryAssemblyFromProteinDomains/tree/main
Owncloud link: https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA

Figure 3A shows the Latent Genetic Potential in terms of protein domains for 96 orthogroups 


## Description of the data and file structure
The 96 orthogroups in this figure have been selected based on two filters which are as follows:
1)	Orthologs in Land Plants (Embryophyta)
2)	Protein Domains in embryophytes and non-Embryophyta species
The purpose to create this is to create a four-dimensional database file with the following parameters:
Species
Stress-annotated Orthogroup
Number of proteins
Embryophytic Domain (in)completion
Example:
column1: Species_X
column2: Orthogroup_N
column3: number of proteins from Orthogroup_N in Species_X
column4: Embryophytic Domain completion(=1, incompletion=0) in Species_X proteome

## Sharing/Access information
DatabaseFiles (Owncloud Link): https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA


## Code/Software
Code part 1: MAKE INTERMEDIATE INPUT FILES
python3 make_intermediate_input_5.py
INPUT FILES REQUIRED:
3_1_input_file_m – from README_Figure1C
all_species_stress_og_fromOrthogroupstsv_37species – Orthogroups.tsv manipulated to give orthogroup ID with respect to the protein ad species
species_ordered_list_final_m – list of 37 species
database_proteindomains – from python3 create_database_proteindomains.py
database_OG3_3_EmbryophyteLCAdomains – from python3 create_database_OG3_3_EmbryophyteLCAdomains.py
OUTPUT:
5_input_file_uniqipr
5_input_file_uniqprot


Code part 2: MAKE FINAL RESULT FILE
python3 make_input_5.py
INPUT FILES REQUIRED:
3_1_input_file_m
all_species_stress_og_fromOrthogroupstsv_37species - Orthogroups.tsv manipulated to give orthogroup ID with respect to the protein ad species
species_ordered_list_final_m - list of 37 species
database_proteindomains - from python3 create_database_proteindomains.py database_OG3_3_EmbryophyteLCAdomains - from python3 create_database_OG3_3_EmbryophyteLCAdomains.py
5_input_file_uniqipr – from Code part 1
5_input_file_uniqprot – from Code part 1
OUTPUT:
5_final_input_file_PROT_DOM_1


Code part 3: MAKING FINAL INPUT FILE TO LOOK AT L.G.P IN EMBRYOPHYTES
FILTERING FINAL RESULT FILE:

Code part 3.1:
	5_3_3OG_input_file_PROT_DOM_1 - obtained by filtering 5_final_input_file_PROT_DOM_1 to extract 2475 stress-annotated orthogroups

Code part 3.2: python3 make_input_6.py
	INPUT FILES REQUIRED:
		species_numbered_list_final_m – list of 37 species
		database_domainfirstappearance – from python3 create_database_domainfirstappearance.py
		database_OGfirstappearance – from python3 create_database_Ogfirstappearance.py
		database_OG3_3_EmbryophyteLCAdomains – from python3 create_database_OG3_3_EmbryophyteLCAdomains.py
	OUTPUT FILES:
		6_filterlessthan_input_file_EmbryophyteLCA
		6_filtergreaterthan_input_file_EmbryophyteLCA
		6_filterequal_input_file_EmbryophyteLCA
	OUTPUT FILE FORMAT:
		column1-orthogroup
		column2-beginning of embryophytic domain set appearance (datatype:integer - from the file species_numbered_list_final_m)
		column3-complete appearance of embryophytic domain set (datatype: integer)
		column4-beginning of appearance of orthologous proteins from orthogroup (datatype:integer)

NOTE: We can now filter the orthogroups whose complete set of embryophytic domains appeared before the appearance of the orthologous proteins

Code part 3.3: 6_filtergreaterthanorequalto_annotation1.1_nonembryophyte_EmbryophyteLCA:
	Column1, column2, column3 and column4 are obtained by filtering (filter: column3<=column4 and column4>=18)
	Column5 (orthogroup functional annotation) obtained from command: python3 make_annotation_6.py

Code part 3.4:
	INPUT FILES REQUIRED:
		5_final_input_file_PROT_DOM_1
	6_filtergreaterthanorequalto_annotation1.1_nonembryophyte_EmbryophyteLCA (column1)
	OUTPUT FILE:
		5_96OG_reorder_new
	FILTER:
	5_96OG_reorder_new obtained by filtering 5_final_input_file_PROT_DOM_1 to extract filtered orthogroups from 6_filtergreaterthanorequalto_annotation1.1_nonembryophyte_EmbryophyteLCA (column1)


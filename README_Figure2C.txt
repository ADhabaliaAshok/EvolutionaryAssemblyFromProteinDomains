Figure 2C

Github link: https://github.com/ADhabaliaAshok/EvolutionaryAssemblyFromProteinDomains/tree/main
Owncloud link: https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA

## Description
Figure 2C shows the weighted distribution of stress annotated protein domains across the 37 species


## Sharing/Access information
DatabaseFiles (Owncloud Link): https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA
The base input file needed is the Stress-annotated orthogroups from Figure 1C Approach 3, and interproscanner files.


## Code/Software
Code part 1: python3 make_input_5_spvsipr_intermediate.py
	INPUT FILES REQUIRED (download from DatabaseFiles link):
		4_input_file_log2 – from README_Figure2A
		database_OG3_3_Orthogroups.tsv – from python3 create_database_OG3_3_Orthogroups.tsv
		database_proteindomains – from python3 create_database_proteindomains.py
	OUTPUT FILES:
		5_input_file_uniqprot_spvsipr
		5_input_file_uniqog_spvsipr

Code part 2: python3 make_input_5_spvsipr.py
	INPUT FILES REQUIRED:
		4_input_file_log2_3_3 – from README_Figure2A
		database_OG3_3_Orthogroups.tsv - from python3 create_database_OG3_3_Orthogroups.tsv
		database_proteindomains - from python3 create_database_proteindomains.py
		5_input_file_uniqprot_spvsipr – from Code part 1
		5_input_file_uniqog_spvsipr – from Code part 1
		species_numbered_list_final_m – 37 species list
	OUTPUT FILES:
		5_final_input_file_log2PROT_OG_1
		5_final_input_file_log2PROT_log2OG_1

Code part 3: python3 sort_5_inputfile.py
	INPUT FILES REQUIRED:
		5_final_input_file_log2PROT_log2OG_1 – from Code part 2
	OUTPUT FILES:
		5_intermediate_input_file_log2PROT_log2OG_sortedPROT_1
		5_intermediate_input_file_log2PROT_log2OG_sortedOG_1

Code part 4: python3 sort_5_finalfile.py
	INPUT FILES REQUIRED:
		5_intermediate_input_file_log2PROT_log2OG_sortedPROT_1 – from Code part 3
		5_intermediate_input_file_log2PROT_log2OG_sortedOG_1 – from Code part 3
		5_final_input_file_log2PROT_OG_1 – from Code part 2
	OUTPUT FILES:
		5_final_input_file_log2PROT_OG_sortPROT_2
		5_final_input_file_log2PROT_OG_sortOG_2

Code part 5: Rscript bubbleheatmap_final_m_spvsipr_sortOG.R
	INPUT FILES REQUIRED:
		5_final_input_file_log2PROT_OG_sortOG_2 – from Code part 4
	OUTPUT FILES:
		5_output_SPvsIPR_log2PROT_OG_sortOG_1.pdf


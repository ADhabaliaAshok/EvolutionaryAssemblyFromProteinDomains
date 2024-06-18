Figure 1B

Github link: https://github.com/ADhabaliaAshok/EvolutionaryAssemblyFromProteinDomains/tree/main
Owncloud link https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA

Figure 1B shows the proteomic details and quality of our dataset of 37 species. Reference proteomes have been downloaded to perform this analysis.


## Description of the data and file structure
This figure is divided into two parts:
BUSCO analysis of proteomes
Number of proteins:
	Proteins
	Proteins annotated by Interproscanner
	Stress Annotated Proteins


## Sharing/Access information
DatabaseFile (Owncloud link): https://owncloud.gwdg.de/index.php/s/dH3Y4MAHSfbmhrA

The input files to create figure are as follows:
BUSCO analysis of proteomes - obtained from Code part 1.1 and Code part 1.2
Number of proteins:
	Proteins - from input fasta file
	Proteins annotated by Interproscanner - from Interproscanner output files
	Number of Stress Annotated Proteins - data file from Figure 1C approach 3


## Code/Software
Final data files:
	figure1_BUSCO.csv
	figure1_table.csv

Code part 1.1: busco -m $MODE -i $IN -o $OUT -f -l chlorophyta_odb10 -o Spinacia_oleracea_BUSCO_out
	IN: fasta file of each of 37 species
	MODE: proteins
	OUT: busco_out

Code part 1.2: Concatanate the complete BUSCO scores (C) for every species into the final data file figure1_BUSCO.csv

Code part 1.3: Create plot to show completeness of BUSCO scores for dataset of 37 species

Code part 2.1: interproscan.sh -i $IN -d /output_directory/ -T /temporary_directory/ -f tsv IN: fasta file of each of 37 species 

Code part 2.2: annotating stress-relevant proteins

Code part 2.3: Concatanate for each species the number of:
	Proteins - from input fasta file
	Proteins annotated by Interproscanner - from Interproscanner output files
	Number of Stress Annotated Proteins - data file from Figure 1C approach 3


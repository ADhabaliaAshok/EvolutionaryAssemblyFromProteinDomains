#!/bin/bash

#SBATCH -p medium
#SBATCH -t 10:00:00
#SBATCH -o Busco_%J.out
#SBATCH -C scratch2
#SBATCH --exclusive
#SBATCH --mem 100G
#SBATCH --mail-type=BEGIN,END
#Delete this line and add your email :)
#SBATCH --mail-user=amradhabalia.ashok@uni-goettingen.de

#Clear everything to create a clean environment 
module purge
#Load busco
module load busco

#Input = fasta file of interest
IN=/usr/users/ashok/OrthologsProject/SpeciesDB/OF_run_remove_them_completely_from_this_dir/Oryza_sativa_v7.0.protein.primaryTranscriptOnly_replaced_ast.fa
#Mode uncomment the one you want to use
#MODE=genome
MODE=proteins
#MODE=transcriptome
#Output folder
OUT=busco_out

#Busco Run
#Auto lineage with only eukaryotic it will find the best eukaryotic database
#busco -m $MODE -i $IN -o $OUT -f --auto-lineage-euk

#Busco with specified lineage selection (eukaryota_odb10) In your case the lineage Iker mentioned :)
busco -m $MODE -i $IN -o $OUT -f -l chlorophyta_odb10 -o Oryza_sativa_BUSCO_out

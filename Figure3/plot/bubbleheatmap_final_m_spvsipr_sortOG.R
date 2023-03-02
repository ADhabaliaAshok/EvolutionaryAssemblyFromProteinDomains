library(viridis)
library(ggplot2)
library(reshape2)
library(viridisLite)

data = read.csv("../result/5_final_input_file_log2PROT_OG_sortOG_2")
names(data) <- c("SPECIES","variable","UPROTEINS","UOG")


level_order_x <- c('Oscillatoria_acuminata','Gloeomargarita_lithophora','Fischerella_thermalis','Trichormus_azollae','Nostoc_punctiforme','Coccomyxa_subellipsoidea','Chlorella_variabilis','Chlamydomonas_reinhardtii','Ulva_mutabilis','Ostreococcus_lucimarinus','Micromonas_pusilla','Mesostigma_viride','Chlorokybus_atmophyticus','Klebsomidium_nitens','Chara_braunii','Mesotaenium_endlicherianum','Spirogloeae_muscicola','Penium_margaritaceum','Anthoceros_punctatus','Anthoceros_agrestis','Marchantia_polymorpha','Physcomitrella_patens','Sphagnum_fallax','Selaginella_moellendorffii','Azolla_filiculoidesFeb12','Picea_abies','Gnetum_montanum','Amborella_trichopoda','Brachypodium_distachyon','Oryza_sativa','Lotus_japonicus','Pisum_sativum','Medicago_truncatula','Brassica_rapa','Arabidopsis_lyrata','Arabidopsis_thaliana','Spinacia_oleracea')

level_order_y <- unique(data[c("variable")])
level_order_y_250 <- head(level_order_y,250)
vect_y <- unlist(level_order_y)
print(vect_y)

coul <- rocket(100)

pdf("5_output_SPvsIPR_log2PROT_OG_sortOG_1.pdf", width=50, height=50)

ggplot(data, aes(x=factor(SPECIES, level = level_order_x), y=factor(variable, level=vect_y))) + geom_point(aes(color = UPROTEINS, size = UOG), alpha=0.6) + scale_color_gradientn(colors=coul, na.value=NA) + geom_text(aes(label=UOG), size=0) + scale_size(range = c(0,20)) + theme(axis.text.x = element_text(colour="grey30", size=10, angle=90, vjust=1, hjust=1), axis.text.y = element_text(colour="grey30", size=5))

dev.off()

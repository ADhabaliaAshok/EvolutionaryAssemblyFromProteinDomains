library(viridis)
library(ggplot2)
library(reshape2)
library(viridisLite)

data = read.csv("../result/5_96OG_reorder_new")
names(data) <- c("SPECIES","variable","UPROTEINS","UDOMAINS")

level_order_x <- c('Oscillatoria_acuminata','Gloeomargarita_lithophora','Fischerella_thermalis','Trichormus_azollae','Nostoc_punctiforme','Coccomyxa_subellipsoidea','Chlorella_variabilis','Chlamydomonas_reinhardtii','Ulva_mutabilis','Ostreococcus_lucimarinus','Micromonas_pusilla','Mesostigma_viride','Chlorokybus_atmophyticus','Klebsomidium_nitens','Chara_braunii','Mesotaenium_endlicherianum','Spirogloeae_muscicola','Penium_margaritaceum','Anthoceros_punctatus','Anthoceros_agrestis','Marchantia_polymorpha','Physcomitrella_patens','Sphagnum_fallax','Selaginella_moellendorffii','Azolla_filiculoidesFeb12','Picea_abies','Gnetum_montanum','Amborella_trichopoda','Brachypodium_distachyon','Oryza_sativa','Lotus_japonicus','Pisum_sativum','Medicago_truncatula','Brassica_rapa','Arabidopsis_lyrata','Arabidopsis_thaliana','Spinacia_oleracea')

level_order_y <- c('OG0041748', 'OG0017442', 'OG0014919', 'OG0012465', 'OG0004683', 'OG0010381', 'OG0011346', 'OG0001843', 'OG0009487', 'OG0008044', 'OG0008225', 'OG0008553', 'OG0008262', 'OG0007074', 'OG0009737', 'OG0008267', 'OG0007745', 'OG0006695', 'OG0003386', 'OG0007901', 'OG0008588', 'OG0004789', 'OG0001973', 'OG0007271', 'OG0010535', 'OG0017110', 'OG0007393', 'OG0001073', 'OG0011429', 'OG0005108', 'OG0009987', 'OG0000623', 'OG0005911', 'OG0000372', 'OG0014086', 'OG0001742', 'OG0001208', 'OG0000148', 'OG0009079', 'OG0000345', 'OG0000163', 'OG0005405', 'OG0001680', 'OG0001200', 'OG0001699', 'OG0007257', 'OG0000429', 'OG0000160', 'OG0001718', 'OG0008690', 'OG0000079', 'OG0013459', 'OG0053735', 'OG0004584', 'OG0000852', 'OG0004972', 'OG0000666', 'OG0002580', 'OG0000521', 'OG0009965', 'OG0001409', 'OG0026114', 'OG0001196', 'OG0000354', 'OG0006063', 'OG0002126', 'OG0000258', 'OG0010000', 'OG0004486', 'OG0006247', 'OG0009080', 'OG0001675', 'OG0001230', 'OG0009131', 'OG0008219', 'OG0002664', 'OG0000147', 'OG0007209', 'OG0001508', 'OG0004197', 'OG0027638', 'OG0009137', 'OG0000512', 'OG0009285', 'OG0008119', 'OG0007926', 'OG0000156', 'OG0000848', 'OG0008965', 'OG0008705', 'OG0002350', 'OG0000657', 'OG0002045', 'OG0002648', 'OG0007512', 'OG0000042')

#level_order_y <- c('OG0000258','OG0010000','OG0008267','OG0007745','OG0007074','OG0017442','OG0001843','OG0012465','OG0011346','OG0041748','OG0008262','OG0009737','OG0009487','OG0010381','OG0014919','OG0008225','OG0008553','OG0004683','OG0008044','OG0007901','OG0001973','OG0006695','OG0004789','OG0003386','OG0001742','OG0004584','OG0000148','OG0001208','OG0005405','OG0001680','OG0000079','OG0009079','OG0000429','OG0000042','OG0007257','OG0013459','OG0001718','OG0053735','OG0006247','OG0009987','OG0005911','OG0000623','OG0017110','OG0010535','OG0011429','OG0007393','OG0001073','OG0007209','OG0000147','OG0004972','OG0000852','OG0001409','OG0002580','OG0009965','OG0000521','OG0000666','OG0000512','OG0026114','OG0000156','OG0001230','OG0009131','OG0000657','OG0001196','OG0002664','OG0008219','OG0000160','OG0009137','OG0000848','OG0009285','OG0004486','OG0000372','OG0007926','OG0002648','OG0002350','OG0000163','OG0000345','OG0008119','OG0002045','OG0001699','OG0008588','OG0008705','OG0001200','OG0008690','OG0014086','OG0007271','OG0000354','OG0002126','OG0006063','OG0009080','OG0005108','OG0001675','OG0004197','OG0008965','OG0001508','OG0027638','OG0007512')
print(level_order_y[58])

coul <- c("#6DB562",rocket(100))

pdf("5_output_3_3OG_y_x_1_reordered_new_new.pdf", width=15, height=15)

ggplot(data, aes(x=factor(SPECIES, level = level_order_x), y=factor(variable, level=level_order_y))) + geom_point(aes(color = UPROTEINS, size = UDOMAINS), alpha=0.8) + scale_color_gradientn(colors=coul, na.value=NA) + geom_text(aes(label=UDOMAINS), size=0) + scale_size(range = c(1,3)) + theme(axis.text.x = element_text(colour="grey30", size=10, angle=90, vjust=1, hjust=1), axis.text.y = element_text(colour="grey30", size=5))

dev.off()

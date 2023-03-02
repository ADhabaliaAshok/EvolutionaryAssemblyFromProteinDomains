library("curl")
library("gplots")
library("dendextend")
library("colorspace")
library("RColorBrewer")
library("colorBlindness")

d = read.csv("../result/7_input_file_log2")
dat_t = t(d)
colnames(dat_t) = dat_t[1,]
dat_t = dat_t[-1,]
dat_n <- apply(dat_t,2,as.numeric)
rownames(dat_n) <- rownames(dat_t)

print(str(dat_n))

dend1 <- as.dendrogram(hclust(dist(dat_n)))
c_group <- 4
dend1 <- color_branches(dend1, k = c_group, col = paletteMartin)
dend1 <- color_labels(dend1, k = c_group, col = paletteMartin)
rMeans <- rowMeans(dat_n, na.rm = T)
dend1 <- reorder(dend1, rowMeans(dat_n, na.rm = T), agglo.FUN = mean)
col_labels <- get_leaves_branches_col(dend1)
col_labels <- col_labels[order(order.dendrogram(dend1))]
dend1 <- set(dend1, "labels_cex", 0.5)
par(cex=5, mar = c(1,1,1,5))

v <- list()
v[[1]] <- 1
for(i in 2:100) v[[i]] <- v[[i-1]] + 0.1095
v[[101]] <- 10.95
v_fin <- c()
for(i in 1:101) v_fin <- c(v_fin,v[[i]])

coul <- c("white",colorRampPalette(brewer.pal(10, "Spectral"))(length(v_fin)-1))

pdf("7_output_file_log2_heatmap.pdf", width=50, height=40)
heatmap.2(dat_n, dendrogram = "row", Rowv = dend1, Colv = "NA", col = coul, trace = "none", density.info = "none", cexRow = 0.2, cexCol = 2.5, xlab = "Species", strCol = 0, adjCol = c(0.5,1), RowSideColors = col_labels, colRow = col_labels, margins=c(20,10), offsetCol = -213)
dev.off()

# EvolutionaryAssemblyFromProteinDomains
**Evolutionary assembly of the plant terrestrialization toolkit from protein domains**
* We want to trace the evolutionary predisposition the green lineage had at the time of terrestrialization.
* Terrestrialization is a complete change in environment from water, and these acted like new and/or intensified stress factors on the green lineage.
* Thus, in order to trace the evolutionary predisposition which led to successful overcoming of challenges of a new environment, we carefully annotate, dissect and analyse the stress proteome of the extant Green lineage.


**Key Concepts**
* Already existing Concept:
    * Orthology
* New/Redefined Concept
    * Embryophytic Domain: Protein domain which has an Embryophytic ancestor, that is, present in at least one Bryophyte species and at least one Tracheophyte species
    * Latent Genetic Potential (LGP): Key (functional) Embryophytic protein domains having Last Common Ancestor (LCA) prior to the LCA of protein with corresponding function


**Data: (Figure 1 A)**
* We take 6 species from Cholorophyte algae lineage, 7 from Streptophyte algae lineage, 5 from Bryophyte lineage and 14 from Tracheophyte lineage. 5 species from Cyanobacteria were taken as an outgroup lineage.


**Stress-annotation (Figure 1B)**
* First 57,796 orthogroups were obtained from 37 proteome. This is computed by using OrthoFinder2.
* Next we need to annotate stress-related proteins across our dataset. Following are existing ways of annotation:
    * Extensive experiments have been done on _A.thaliana_ and _P.patens_ in the green lineage. Thus, we stress-annotated 37 proteomes using TAIR10 and PEATmoss respectively. From this method, we stress-annotated 4,902 orthogroups
    * Eggnogmapper is a known tool with an extensive database used for gene ontology purposes. We stress-annotated 17,349 orthogroups.
* In order to avoid experimental bias and tool-based randomness we overlap the two methods to have our final stress-annotation. We finally filtered 2,475 stress-annotated orthogroups from 57,796 orthogroups.


**Overview of Stress-annotation (Figure 1C, 1D)**
* To have an overview of stress-annotation, overlaps of stress-annotated protein domains, proteins and orthogroups across our dataset lineages and various response to stresses are shown.


**Distribution of Stress-annotation (Figure 2)**
* Using the overlap annotation approach explained earlier, the stress-annotated orthogroups and corresponding protein domains are in Figure 2A. A standard pattern is observed in both, that is, the unique number of stress orthogroups and protein domains increase from Cyanobacteria to Tracheophytes. The number of proteins and average number of protein domains also increases similarly.
* Top 10 bursts of protein domains from one lineage to the next is shown in Figure 2B.


**Changes in stress-annotation with respect to Protein Domains (Figure 3)**
* Figure 3 is a 4-dimensional plot with the following parameters: Species(37), Protein Domains (100), Number of Orthgogroups with Protein Domain (size of circle), Number of Proteins with Protein Domain (Color of circle). The plot is sorted from top to bottom based on the number of orthogroups, and the top 100 protein domains are chosen for the plot.
* This plot is used to express an overview of the most significant occurances of sub- and neo-functionalizations. Here, each orthogroup is considered to be a protein family. 2 protein families can have an overlapping number of functions. That is why there are more than 1 orthogroup which have the same protein domain.


**Assembling LGP from protein domains (Figure 4) - refer to Key Concepts for to understand LGP**
* In Figure 1A, we show 2 categories (x/y) of orthogroups at each node (a,b,c,d,e,f). The number **y** for example at node **b** indicates the number of orthogroups (4) in Tracheophyta+Bryophyta+Zygnemaotphyceae that have LGP (or key Embryophytic protein domains) in Charophyceae. The number **x** at node **b** indicates the number of orthogroups (131) in Tracheophyta+Bryophyta+Zygnemaotphyceae that have LGP in all the rest of the lineages in the figure.
* Since we are concerned about the LGP for Land Plants (Embryophytes), we look at node **a**. Next, we functionally annotate 96 orthogroups. 50 annotations that occur the most number of times is shown in Figure 4B.
* In Figure 4C, we can see in which species the key Embryophytic Domains are present whose proteins and protein families are only seen in Embryophytes.

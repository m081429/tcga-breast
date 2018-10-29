library('arsenal')

Data=read.table("phenotype_data/phenotypes_withSet.tsv",sep="\t")

# Keep only selected Columns
KEEPERS = c("age_at_initial_pathologic_diagnosis","race","ajcc_pathologic_tumor_stage","histological_type","initial_pathologic_dx_year","vital_status","tumor_status","PFI","PFI.time","ER.Status","PR.Status","HER2.Final.Status","Metastasis.Coded","PAM50.mRNA","Set","ATM_Mutations","BRCA1_Mutations","BRCA2_Mutations","CDH1_Mutations","CDKN2A_Mutations","PTEN_Mutations","TP53_Mutations","AnyGene_Mutations","age_at_initial_pathologic_diagnosis","race")

Data$Set[sample(x=nrow(Data),size=nrow(Data)*.2)]="Test"

tmp = na.omit(Data[,KEEPERS])

# Remove variables with not enough info
tmp = tmp[-which(tmp$race=="AMERICAN INDIAN OR ALASKA NATIVE"),]
tmp$race = as.factor(as.character(tmp$race))
tmp = tmp[-which(tmp$ajcc_pathologic_tumor_stage=="[Discrepancy]"),]
tmp$ajcc_pathologic_tumor_stage = as.factor(as.character(tmp$ajcc_pathologic_tumor_stage))

tmp$ajcc_pathologic_tumor_stage = as.factor(gsub("A|B|C","",as.character(tmp$ajcc_pathologic_tumor_stage)))
tmp = tmp[which(tmp$histological_type=="Infiltrating Ductal Carcinoma"|tmp$histological_type=="Infiltrating Lobular Carcinoma"),]
tmp$histological_type = as.factor(as.character(tmp$histological_type))


summary(tableby(Set ~.,data=Data))

write.table(tmp,file="phenotype_data/phenotypes_withSet.tsv",row.names=FALSE,sep="\t")

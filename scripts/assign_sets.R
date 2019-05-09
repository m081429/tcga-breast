library('arsenal')

# The purpose of this sript is to randomly assign samples to groups for training and testing

Data=read.csv("phenotype_data/phenotypes.clean.tsv",sep="\t",header=TRUE)
Data$type=NULL

# Assign rownames
rownames(Data)=Data$bcr_patient_barcode
Data$bcr_patient_barcode=NULL

# Assign to training or testing
Data$Set="Train"
Data$Set[sample(x=nrow(Data),size=nrow(Data)*.2)]="Test"

# Verify groups are diverse and balanced
summary(tableby(Set ~.,data=Data))

write.csv(Data,file="phenotype_data/phenotypes_withSet.tsv",row.names=TRUE)

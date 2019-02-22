Features to have in TFRecords


## Categorical

- race
  - 0: White
  - 1: Black
  - 2: Asian

- ajcc_pathologic_tumor_stage
  - 0: StageX
  - 1: Stage1
  - 2: Stage2
  - 3: Stage3
  - 4: Stage4

- pam50_mRNA
  - 0: Basal
  - 1: HER2
  - 2: LumA
  - 3: LumB
  - 4: Normallike

- histological_type
  - 0: Normal (None are in BreakHis, none of the rest are in BACH)
  - 1: adenosis              (A)
  - 2: fibroadenoma          (F)
  - 3: phyllodes_tumor       (PT)
  - 4: tubular_adenoma       (TA)
  - 5: ductal_carcinoma      (DC)
  - 6: lobular_carcinoma     (LC)
  - 7: mucinous_carcinoma    (MC)
  - 8: papillary_carcinoma   (PC)
  - 9: other/unknown

- tissue_pathology:
  - 0: Normal   (None are in BreakHis)
  - 1: Benign   (any Benign in BreakHis)
  - 2: InSitu   (None are in BreakHis)
  - 3: Invasive (any Malignant in BreakHis)

## Binary
With the exception of `tumor_class`, all these variables come from the `phenotype_data/phenotypes_withSet.tsv` file.

- tumor_class
  - 0: Benign
  - 1: Malignant 

- tumor_status
  - 0: TUMOR FREE
  - 1: WITH TUMOR

- DeadInFiveYrs
  - 0: No
  - 1: Yes

- ER_Status
  - 0: Negative
  - 1: Positive

- PR_Status
  - 0: Negative
  - 1: Positive

- HER2_Status
  - 0: Negative
  - 1: Positive

- Metastasis_Coded
  - 0: Negative
  - 1: Positive

- ATM_Mutations
  - 0: Negative
  - 1: Positive

- BRCA1_Mutations
  - 0: Negative
  - 1: Positive

- BRCA2_Mutations
  - 0: Negative
  - 1: Positive

- CDH1_Mutations
  - 0: Negative
  - 1: Positive

- CDKN2A_Mutations
  - 0: Negative
  - 1: Positive

- PTEN_Mutations
  - 0: Negative
  - 1: Positive

- TP53_Mutations
  - 0: Negative
  - 1: Positive

- AnyGene_Mutations
  - 0: Negative
  - 1: Positive


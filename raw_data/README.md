Downloaded [data](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.cases.primary_site%22%2C%22value%22%3A%5B%22Breast%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.data_type%22%2C%22value%22%3A%5B%22Slide%20Image%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22files.experimental_strategy%22%2C%22value%22%3A%5B%22Diagnostic%20Slide%22%5D%7D%7D%5D%7D)


We also donloaded data from the [BACH challenge](https://arxiv.org/pdf/1808.04277.pdf).

And [BreakHis](https://web.inf.ufpr.br/vri/databases/breast-cancer-histopathological-database-breakhis/)
```
https://rdm.inesctec.pt/dataset/604dfdfa-1d37-41c6-8db1-e82683b8335a/resource/df04ea95-36a7-49a8-9b70-605798460c35/download/breasthistology.zip # BACH
http://www.inf.ufpr.br/vri/databases/BreaKHis_v1.tar.gz # BreakHis
```


# Goal
Identify pixels in breast cancer tissues that are tumor.

# Folders
1. XML_TCGA_HG/	# has a single XML file for each sample with coordinates for the tumor regions
		# Cruz-Roa et al [(2018)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0196828)
2. TCGA/ 	# Actual images from Cruz-Roa

3. BACH/	# dataset from bach challenge


# Datasets


BACH/
├── breasthistology.zip
├── Code [7]
├── Test_data [37]
└── Training_data
    ├── Benign [71]
    ├── In Situ [63]
    ├── Invasive [62]
    └── Normal [55]

BrekHis
├── benign			#Patients	#Images
    ├── adenosis 		4		106		
    ├── fibroadenoma    	10		237
    ├── phyllodes_tumor 	3		115
    └── tubular_adenoma 	7		130
├── malignant
    ├── ductal_carcinoma        38		788
    ├── lobular_carcinoma       5		137
    ├── mucinous_carcinoma      9		169
    └── papillary_carcinoma     6		138


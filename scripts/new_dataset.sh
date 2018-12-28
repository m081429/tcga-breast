#creating validation image patch from tcga
#/usr/local/bin/python3 /data/Naresh_Learning/scripts/XML_annotations_shapely2_debug.py -i /data/projects/breast/raw_data/XML_TCGA_HG/TCGA-BH-A18H-01Z-00-DX1.4EC9108F-04C2-4B28-BD74-97A414C9A536.xml -s /data/projects/breast/raw_data/TCGA/svs/7edf7f7c-5001-4374-b5e1-bf8d680c8a1d/TCGA-BH-A18H-01Z-00-DX1.4EC9108F-04C2-4B28-BD74-97A414C9A536.svs -p /data/Naresh_Learning/scripts/patches1/ -n TCGA-BH-A18H-01Z-00-DX1
#/usr/local/bin/python3 /data/Naresh_Learning/scripts/XML_annotations_shapely2_debug.py -i /data/projects/breast/raw_data/XML_TCGA_HG/TCGA-BH-A0BO-01Z-00-DX1.1A704471-FEB3-40F9-9838-3E347A18285F.xml -s /data/projects/breast/raw_data/TCGA/svs/17e93222-011d-4a1f-a12e-472825697904/TCGA-BH-A0BO-01Z-00-DX1.1A704471-FEB3-40F9-9838-3E347A18285F.svs -p /data/Naresh_Learning/scripts/patches1/ -n TCGA-BH-A0BO-01Z-00-DX1 
#/usr/local/bin/python3 /data/Naresh_Learning/scripts/XML_annotations_shapely2_debug.py -i /data/projects/breast/raw_data/XML_TCGA_HG/TCGA-AR-A1AM-01Z-00-DX1.B3F006D9-9386-41E5-B0B1-B0832EE104A0.xml -s /data/projects/breast/raw_data/TCGA/svs/df8c86dd-0afa-491f-8d6d-939830044367/TCGA-AR-A1AM-01Z-00-DX1.B3F006D9-9386-41E5-B0B1-B0832EE104A0.svs -p /data/Naresh_Learning/scripts/patches1/ -n TCGA-AR-A1AM-01Z-00-DX1 
#create image patches from external sources
#python3 XML_annotations_shapely_newdataset.py
#python3 XML_annotations_shapely_BACH_BreakHIS.py
python3 XML_annotations_shapely_BACH_BreakHIS_create_tf.py

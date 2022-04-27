## 1 download and create dataset

Dataset available here:
https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics
Use dicom_to_nifti.ipynb first to transform the dicom into niftii
Use create_dataset.ipynb then to transform niftii into the dataset (.npy) for traing

OR -

## 1 (EASIEST WAY) bis - use directly the dataset in the drive

download in the repository in the dir data/ the directory data/dataset from the drive
Then-

## 2 - training and testing
For machine learning, use feature_extraction.py
For Deep learning, everything is in the main.ipynb.

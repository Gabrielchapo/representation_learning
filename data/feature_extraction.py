from radiomics import featureextractor
import glob
import pandas as pd

import argparse

import logging
logger = logging.getLogger("radiomics.glcm")
logger.setLevel(logging.ERROR)


def extraction(name):
    file_path = "data/extracted_"+name+"+normalize+removeOutliers.csv"

    all_images = sorted(glob.glob("data/preprocessed/img/*"))
    all_seg = glob.glob("data/preprocessed/seg/*")
    all_extractions = []

    for image in all_images:
        print(image[-13:-4])
        corresponding_seg = [x for x in all_seg if image[-13:-4] in x and name in x]
        if len(corresponding_seg) > 0:
            for seg in corresponding_seg:
                print(seg[22:])
                extractor = featureextractor.RadiomicsFeatureExtractor("data/params.yml")
                try:
                    extraction = extractor.execute(image, seg)
                    extraction = dict(extraction)
                    extraction["PatientID"] = image[-13:-4]
                    all_extractions.append(extraction)
                except:
                    print("erreur ici")
                
        else:
            print("no seg available for this patient")
            
    df = pd.DataFrame(all_extractions)
    df.to_csv(file_path)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', "--part", type=str, choices=["GTV", "Esophagus", "Spinal", "Left", "Right", "Total"], required=True)
    args = vars(parser.parse_args())
    extraction(args["part"])


import os 
import sys
import shutil
from tqdm import tqdm
import argparse

# svs_path = r'/home/sci/Disk2/tcga_brca/WSI'
svs_path = r'/home/sci/Disk2/tcga_brca/WSI/tcga_brca/pyramid/sci'
patch_path = r'/home/sci/Disk2/tcga_brca/WSI/tcga_brca/single/sci'
slide_list = tqdm(os.listdir(svs_path))
# print(slide_list)
if not os.path.exists(os.path.join(svs_path,'tcga_brca','0')):
    normal_path = os.path.join(svs_path, 'tcga_brca','0')
    os.makedirs(normal_path)
if not os.path.exists(os.path.join(svs_path,'tcga_brca','1')):
    tumor_path = os.path.join(svs_path, 'tcga_brca','1')
    os.makedirs(tumor_path)


parser = argparse.ArgumentParser(description = 'trasfer wsi to classification file')
parser.add_argument('--svs_path', type = str)

def main(args): 
    for slide in slide_list:
        slide_list.set_description('Precessing %s' % slide)
        file_path = os.path.join(args.svs_path, slide)
        if slide[13] == '0':
            shutil.move(file_path,tumor_path)
        else:
            shutil.move(file_path,normal_path)


        

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
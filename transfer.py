import os 
import sys
import shutil
from tqdm import tqdm

svs_path = r'/home/sci/Disk2/tcga_brca/WSI'
slide_list = tqdm(os.listdir(svs_path))
# print(slide_list)
if not os.path.exists(os.path.join(svs_path,'tcga_brca','normal')):
    normal_path = os.path.join(svs_path, 'tcga_brca','normal')
    os.makedirs(normal_path)
if not os.path.exists(os.path.join(svs_path,'tcga_brca','tumor')):
    tumor_path = os.path.join(svs_path, 'tcga_brca','tumor')
    os.makedirs(tumor_path)




def main(): 
    for slide in slide_list:
        slide_list.set_description('Precessing %s' % slide)
        file_path = os.path.join(svs_path, slide)
        if slide[13] == '0':
            shutil.move(file_path,tumor_path)
        else:
            shutil.move(file_path,normal_path)
        

if __name__ == '__main__':
    main()
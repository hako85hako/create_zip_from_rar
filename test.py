import rarfile
import zipfile
import shutil
import glob
import os
import sys
def test():
 ###ここから下がおかしい
    ###空のzipファイルができてしまう
    now_folder = os.getcwd()
    files = os.listdir(now_folder)
    files_dirs = [f for f in files if os.path.isdir(os.path.join(now_folder, f))]
    for files_dir in files_dirs:
        #print(files_dir)
        if files_dir == 'rarfile' or files_dir == 'mangaRegister':
            print(files_dir+'：スルーしました')
        else:
            with zipfile.ZipFile(files_dir+'.zip','w') as myzip:
                for image in os.listdir(f'{now_folder}/{files_dir}'):    
                    myzip.write(f'{files_dir}/{image}')
                shutil.rmtree(files_dir)         
if __name__=="__main__":
    test()
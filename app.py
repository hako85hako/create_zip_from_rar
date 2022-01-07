import rarfile
import zipfile
import shutil
import glob
import os
import sys


def test():
    #初期設定####################################################################################################
    args = sys.argv
    total_file_size = 0
    file_names = glob.glob('*.rar')
    print(file_names)
    now_folder = os.getcwd()
    print(now_folder)
    #new_dir_path = '/Users/sakaiyuunin/Library/Mobile Documents/com~apple~CloudDocs/漫画/'
    ###########################################################################################################
    print(now_folder)
    print(file_names)
    #rar形式のファイルを展開する
    for file_name in file_names:
        rf = rarfile.RarFile(file_name)
        #print(rarfile.getcwd())
        rf.extractall()
        
        os.remove(file_name)
        for f_fire_name in rf.infolist():
            #print(f_fire_name.filename, f_fire_name.file_size)
            total_file_size += f_fire_name.file_size     
    if glob.glob('*.rar'):
    #rar形式のファイルを展開する
        file_names2 = glob.glob('*.rar')
        for file_name2 in file_names2:
            rf = rarfile.RarFile(file_name2)
            rf.extractall()
            os.remove(file_name2)
            for f_fire_name2 in rf.infolist():
                #print(f_fire_name2.filename, f_fire_name2.file_size)
                total_file_size += f_fire_name2.file_size  
    
    print(total_file_size/1000000)
    print('MByte')

    now_folder = os.getcwd()
    files = os.listdir(now_folder)
    files_dirs = [f for f in files if os.path.isdir(os.path.join(now_folder, f))]
    for files_dir in files_dirs:
        #print(files_dir)
        if files_dir == 'rarfile' or files_dir == 'mangaRegister':
            print(files_dir+'：スルーしました')
        else:
            #print(files_dir)
            #tests = glob.glob('.\mangaRegister/'+files_dir+'/0001.jpg')
            with zipfile.ZipFile(files_dir+'.zip','w') as myzip:
                for image in os.listdir(f'{now_folder}/{files_dir}'):    
                    myzip.write(f'{files_dir}/{image}')
                shutil.rmtree(files_dir)           
               
if __name__=="__main__":
    test()

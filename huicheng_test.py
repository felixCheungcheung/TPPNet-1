import os
import sys
import subprocess

file_path = 'D:\HUICHENG\Code_Maintainance\TPPNet\data\SHS100K_url'
storage_path = 'D:\HUICHENG\Code_Maintainance\TPPNet\crawl_data\shs_data'
with open(file_path,encoding ='gb18030',errors = 'ignore') as fp:
    file_list = [line.rstrip() for line in fp]
print(len(file_list))
count = 0 
success_id = []
failed_id = []
with open(os.path.join(storage_path,'log_success.txt'),'r') as f1:
    
    success_id = [line.rstrip() for line in f1]
with open(os.path.join(storage_path,'log_failed.txt'),'r') as f2:
    failed_id = [line.rstrip() for line in f2]


for i in range(len(file_list)):
    
    file = file_list[i].split('	')
    set_id = file[0]
    ver_id = file[1]
    video_title = set_id +"_"+ ver_id
    output_path = os.path.join(storage_path,video_title+'.mp3')
    print(os.path.exists(output_path))
    if os.path.exists(output_path):
        continue

    elif video_title in failed_id:
        continue
    else:
        try:
            yt_link = 'http:'+file[4]
            print(yt_link)
            cmd = ('youtube-dl -o {} -f bestaudio {} -i').format(output_path, yt_link)
            subprocess.check_call(cmd,shell=True)
            success_id.append(video_title)

        except:
            failed_id.append(video_title)

                
            continue
    if (i+1) % 10 == 0:
        with open(os.path.join(storage_path,'log_success.txt'),'w') as f1:
            for s in success_id:
                f1.write(s+'\n')
        with open(os.path.join(storage_path,'log_failed.txt'),'w') as f2:
            for s in failed_id:
                f2.write(s+'\n')




print(success_id)
print(failed_id)
# Generate CQT from wavefile
# Save as npy

import librosa
import numpy as np
import os
from multiprocessing import Pool
from tqdm import tqdm

in_dir = 'crawl_data/shs_data/'
out_dir = 'youtube_cqt_npy/'


def CQT(args):
    try:
        in_path, out_path = args
        data, sr = librosa.load(in_path)
        if len(data)<1000:
            return
        cqt = np.abs(librosa.cqt(y=data, sr=sr))
        mean_size = 20
        height, length = cqt.shape
        new_cqt = np.zeros((height,int(length/mean_size)),dtype=np.float64)
        for i in range(int(length/mean_size)):
            new_cqt[:,i] = cqt[:,i*mean_size:(i+1)*mean_size].mean(axis=1)
        np.save(out_path, new_cqt)
        #print(new_cens.shape)
    except :
        print('wa', in_path)
# CQT FUNC看起来是down sampling
        
params =[]
for ii, (root, dirs, files) in tqdm(enumerate(os.walk(in_dir))):  
    if ii < 5000: continue
    if len(files):
        for file in files:
            in_path = os.path.join(root,file)
            set_id = root.split('/')[-1]
            out_path = out_dir + set_id + '_' + file.split('.')[0] + '.npy'
            params.append((in_path, out_path))

print('begin')
pool = Pool(4) # 40核机器
pool.map(CQT, params)
pool.close()
pool.join()



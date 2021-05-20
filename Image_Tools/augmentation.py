#!/usr/bin/env python
# coding: utf-8

# In[12]:

import beepy as beep
import os
import argparse
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


# In[13]:


parser=argparse.ArgumentParser()
parser.add_argument("-d","--dir",help="Enter the directory",type=str,required=True)
parser.add_argument("-m","--multiplier",help="Number of augmentations for each image",type=int,required=True)
args=parser.parse_args()


# In[6]:


dir=args.dir


# In[3]:


files=os.listdir(dir)
files.sort()


# In[4]:


datagen = ImageDataGenerator(
          rotation_range=10,
          width_shift_range=0.05,
          height_shift_range=0.05,
          shear_range=0.2,
          zoom_range=0.1,
          horizontal_flip=True,
          vertical_flip=True,
          fill_mode='nearest',
          brightness_range=(0.2,0.8)
)


# In[10]:


for f in range(len(files)):
    f_name=dir+files[f]
    img=load_img(f_name)
    x=img_to_array(img)
    x=x.reshape((1,)+x.shape)
    
    fn=files[f]
    fn=fn.replace('.jpeg','')
    fn=fn.replace('.jpg','')
    fn=fn.replace('.JPG','')

    i=1
    pre="{fn}_aug{i}".format(fn=fn,i=i)
    for batch in datagen.flow(x,batch_size=1,save_to_dir=dir,save_prefix=pre,save_format='jpeg'):
        i+=1
        
        if i>args.multiplier:
            break
beep.beep(sound="ping")

# In[ ]:






# coding: utf-8

# In[1]:


# Q2
# 讀取 westbrook.jpg
# 將每個pixel的RGB數值都減半（ex: (122, 244, 245）->(61, 122, 122)），再將圖片輸出為 Q2.jpg
# RGB數值記得要去掉小數點！(無條件捨去)


# In[31]:


from PIL import Image
img = Image.open("westbrook.jpg")
print(img.format, img.size, img.mode)


# In[34]:


pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]): 
        pixels[i,j] = (round(pixels[i, j][0] / 2), round(pixels[i, j][1] / 2),  round(pixels[i, j][2] / 2))
        
img.save("Q2.jpg")
img.close()


# In[35]:


# Q2 Done


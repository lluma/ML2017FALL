
# coding: utf-8

# In[16]:


words = open("words.txt", "r")
content = str.split(words.read())
print(content)


# In[27]:


spliter = []
counter = []
for s in content:
    if spliter.count(s) == 0:
        spliter.append(s)
        counter.append(1)
    else:
        counter[spliter.index(s)] += 1
print(spliter)
print(len(content), len(spliter))
print(counter)


# In[38]:


words.close()
Q1 = open("Q1.txt", "w")
for i in range(len(spliter)):
    Q1.write("%s %d %d\n" % (spliter[i], i, counter[i]))
Q1.close()


# In[ ]:


# Q1 Done
# 讀取words.txt中的所有英文單字，英文單字之間皆由<space>做分隔
# 按照單字出現的順序，給予編號（0, 1, 2 ...）。 (不要跳號)
# 計算單字出現的次數。
# 將得到編號和次數，由單字出現在words.txt的順序輸出至
# Q1.txt，最後一行不要換行，每一行皆為：<單字><space><編號><space><出現次數>
# Ntu, ntu 為不同單字


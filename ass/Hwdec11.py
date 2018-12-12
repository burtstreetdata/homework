#!/usr/bin/env python
# coding: utf-8

# In[33]:


def cubstreak (file, tname):
    s=0
    longstreak=0
    with open (file) as k:
        games=k.readlines()
        for line in games:
            fields=line.split(",")
            if tname in line:
                
                if fields[3].strip('"')==tname:
                  #  print ("TURKEY")
                    if fields[9] > fields [10]:
                        s+=1
                   #     print (s)
                        if s>longstreak:
                            longstreak=s
                    else:
                        s=0

                if fields[6].strip('"')==tname:
                    if fields [10] > fields [9]:
                        s+=1
                    #    print (s)
                        if s>longstreak:
                            longstreak=s
                    else:
                        s=0
            else:
                pass
            
    return longstreak


# In[39]:


cubstreak ('C:/TMP/gl2018/gl2018.txt', "CHN")


# In[5]:


cubstreak ('C:/TMP/gl2018/gl2018.txt')


# In[13]:


def listnames(file):
    u=list()
    with open (file) as k:
          for line in k:
            fields=line.split(",")
            sf3=fields[3].strip('"')
            sf6=fields[6].strip('"')
            if sf3 not in u:
                u.append(sf3)
            if sf6 not in u:
                u.append(sf6)
    return u


# In[14]:


listnames('C:/TMP/gl2018/gl2018.txt')


# In[76]:


file='C:/TMP/gl1935.txt'


# In[77]:


file


# In[78]:


teams=listnames(file)


# In[79]:


def sbyr(file):
    longstreak=0
    btm=""
    for t in teams:
        strk=cubstreak(file, t)
        if strk>longstreak:
            longstreak=strk
            btm=t
    #print (longstreak, btm)
    return (longstreak, btm)


# In[80]:


sbyr(file)


# In[ ]:





# In[ ]:





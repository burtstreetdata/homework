#!/usr/bin/env python
# coding: utf-8

# In[52]:



def list_names(filename, filename2):
    i=0
    htr=0
    atr=0
    u=list()
    with open (filename) as f:
         for g in f.readlines():
                fields=g.split(',')
                i+=1
                htr+= int(fields[9])
         #       print (fields [9])
         ha= (htr/i)
         with open (filename2) as f2:
           for l in f2.readlines():
                fields2=l.split(',')
           if (fields[3]) not in f.readlines():
               print ((fields[3]))
           else:
               print ('gobble gobble') 
   


# In[53]:


list_names('C:/TMP/GL1935.TXT', 'C:/TMP/gl2018/GL2018.txt')


# In[54]:


oteams


# In[55]:


cteams


# In[11]:


for line in oteams:
    if line in cteams:
        print (line)
        
    else:
        pass


# In[12]:


cteams


# In[13]:


list_names('C:/TMP/gl1935.txt')


# In[69]:


def gobbler (file):
    i=0
    homescore=0
    awayscore=0
    with open (file) as doc:
        doc.readlines()
        for line in doc:
            fields= line.split(",")
            homescore+=int(fields[3])
            awayscore+=int(fields[4])
            i+=1
            print (homescore+awayscore/i)
    print ('gobble')


# In[70]:


gobbler ('C:/TMP/gl2018/gl2018.txt')


# In[ ]:





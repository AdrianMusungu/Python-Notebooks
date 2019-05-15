#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


#creating an array of range 10
a = np.arange(10)
print (a)


# In[6]:


#reshaping the array to be 2D in nature
b = a.reshape(5,2)
print (b)


# In[23]:


#the flat function: behaves similar to Python's iterator
f = np.arange(0,10,3).reshape(2,2)
print (f)
print('The flat function:')
print (f.flat[3])


# In[20]:


#Flattening an array
f1 = f.flatten()
print(f1)


# In[26]:


#Flattening an array with a custom ordering
f2 = f.flatten(order = 'F')
print(f2)


# In[28]:


#flatten returns a copy whereas ravel returns a view of the original
#if you modify a ravel(), it may change the elements of the original array
#this doesnt happen with flatten()
f3 = f.ravel()
print(f3)


# In[33]:


#transpose an array
t = np.arange(9).reshape(3,3)
print (t)
print ('\n The transpose is:')
print (np.transpose(t))


# In[41]:


#broadcasting
arr = np.arange(5)
print('original:')
print (arr)
br = np.broadcast_to(arr, (5,5))
print('\n broadcast:')
print(br)


# In[47]:


#concatenating arrays
a1 = np.array([['a','b'],['c','d']])
a2 = np.array([['e','f'],['g','h']])

print ('Array 1 : \n', a1)
print ('Array 2 : \n', a2)
print ('\n')
print('joining along axis 0 : \n')
print(np.concatenate((a1,a2)), '\n')
print('joining along axis 1 : \n')
print(np.concatenate((a1,a2), axis = 1))


# In[48]:


#stacking arrays
print('stacking along axis 0 : \n')
print(np.stack((a1,a2)), '\n')
print('stacking along axis 1 : \n')
print(np.stack((a1,a2), axis = 1))


# In[51]:


#horizontal stacking vs vertical stacking: replicates concatenating
print('vertical stacking: \n')
print(np.vstack((a1,a2)), '\n')
print('horizontal stacking: \n')
print(np.hstack((a1,a2)))


# In[54]:


#splitting arrays
arr2 = np.arange(10)
s = np.split(arr2, 2)
print('\n original:', arr2)
print('\n split in 2 equal parts: \n', s)


# In[56]:


#horizontal vs vertical array splitting
arr3 = np.arange(16).reshape(4,4)
vs = np.vsplit(arr3,2)
hs = np.hsplit(arr3,2)
print('original: \n', arr3, '\n')
print('vertical splitting: \n',vs, '\n')
print('horizontal splitting: \n',hs)


# In[58]:


#resizing arrays
x = np.array([[1,2],[3,4],[5,6]])
rs1 = np.resize(x,(3,2))
rs2 = np.resize(x, (3,3))
#take note of what happens to rs2
print('original: \n', x, '\n')
print('resized to shape(3,2): \n', rs1, '\n')
print('resized to shape(3,3): \n', rs2)


# In[62]:


#Appending to arrays
ap0 = np.append(x,[7,8])
ap1 = np.append(x,[[7,8]], axis=0)
ap2 = np.append(x,[[1,1],[2,2],[3,3]], axis =1)
print('original: \n', x, '\n')
print('simple append: \n', ap0, '\n')
print('append along axis 0: \n', ap1, '\n')
print('append along axis 1: \n', ap2, '\n')


# In[ ]:


#inserting 


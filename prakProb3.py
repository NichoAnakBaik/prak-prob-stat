#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data_nicho = pd.read_clipboard()

# Menampilkan data
print(data_nicho)


# In[3]:


nicho = data_nicho[data_nicho['Bedrooms'] == 2]

# Menampilkan nama
print(nicho)


# In[5]:


nicho['Bathrooms'] = pd.to_numeric(nicho['Bathrooms'])

import numpy as np

nicho['Bathrooms'] = nicho['Bathrooms'].apply(lambda x: 'large' if x > 2 else 'small')

# Menampilkan DataFrame setelah modifikasi
print(nicho)


# In[6]:


import numpy as np

nicho['newvariable'] = np.where(nicho['Offers'] > 2, 'large', 'small')

# Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(nicho)


# In[7]:


# Menambahkan kolom baru 'newvariable' 
nicho['newvariable'] = nicho['Price'] / nicho['SqFt']

# Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(nicho)


# In[8]:


nicho = nicho.drop(columns=['newvariable'])

# Menampilkan DataFrame 'nama' 
print(nicho)


# In[9]:


kolom1dan2 = data_nicho.iloc[:, 0:2]

# Menampilkan DataFrame kolom1dan2
print(kolom1dan2)


# In[10]:


# Memilih kolom 1 dan 2 dari DataFrame data_nama
kolom3dan4 = data_nicho.iloc[:, 2:4]

# Menampilkan DataFrame kolom3dan4
print(kolom3dan4)


# In[11]:


# Menggabungkan dua DataFrame 
kolom1sd4 = pd.concat([kolom1dan2, kolom3dan4], axis=1)

# Menampilkan DataFrame kolom1sd4
print(kolom1sd4)


# In[14]:


# Menggabungkan baris dari dua DataFrame
baris1sd3 = data_nicho.iloc[0:3, :]
baris4sd6 = data_nicho.iloc[3:6, :]
baris1sd6 = baris1sd3.append(baris4sd6)

# Menampilkan DataFrame baris1sd6
print(baris1sd6)


# In[15]:


# Import pandas library
import pandas as pd

# Menggabungkan baris dari dua DataFrame
baris1sd3 = data_nicho.iloc[0:3, :]
baris4sd6 = data_nicho.iloc[3:6, :]
baris1sd6 = pd.concat([baris1sd3, baris4sd6])

# Menampilkan DataFrame baris1sd6
print(baris1sd6)


# In[16]:


data_nicho_sort = data_nicho.sort_values(by='Price')

print(data_nicho_sort)


# In[27]:


import pandas as pd

data_nicho = pd.read_clipboard()

# Menampilkan data
print(data_nicho)


# In[29]:


nicho = data_nicho[data_nicho['tinggi badan'] == 170 ]

# Menampilkan nama
print(nicho)


# In[30]:


nicho['tinggi badan'] = pd.to_numeric(nicho['tinggi badan'])

import numpy as np

nicho['tinggi badan'] = nicho['tinggi badan'].apply(lambda x: 'Tinggi' if x > 160 else 'Pendek')

# Menampilkan DataFrame setelah modifikasi
print(nicho)


# In[31]:


import numpy as np

nicho['Jurusan'] = 'Infor20'
nicho['Fakultas'] = 'FTI'

# Menampilkan DataFrame 'nama' setelah penambahan kolom baru
print(nicho)


# In[32]:


nicho = nicho.drop(columns=['Fakultas'])

# Menampilkan DataFrame 'nama' 
print(nicho)


# In[33]:


kolom1dan2 = data_nicho.iloc[:, 0:2]

# Menampilkan DataFrame kolom1dan2
print(kolom1dan2)


# In[34]:


# Memilih kolom 1 dan 2 dari DataFrame data_nama
kolom3dan4 = data_nicho.iloc[:, 2:4]

# Menampilkan DataFrame kolom3dan4
print(kolom3dan4)


# In[35]:


# Menggabungkan dua DataFrame 
kolom1sd4 = pd.concat([kolom1dan2, kolom3dan4], axis=1)

# Menampilkan DataFrame kolom1sd4
print(kolom1sd4)


# In[36]:


# Import pandas library
import pandas as pd

# Menggabungkan baris dari dua DataFrame
baris1sd5 = data_nicho.iloc[0:5, :]
baris25sd30 = data_nicho.iloc[24:31, :]
baris1sd5dan25sd30 = pd.concat([baris1sd5, baris25sd30])

# Menampilkan DataFrame baris1sd6
print(baris1sd5dan25sd30)


# In[37]:


data_nicho_sort = data_nicho.sort_values(by='waktu perjalanan')

print(data_nicho_sort)


# In[ ]:





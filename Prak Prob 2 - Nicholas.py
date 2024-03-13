#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [1, 2, -5, 0.3, 6, -2, 4]  # numeric vector
b = ["one", "two", "three"]     # character vector
c = [True, True, True, False, True]  # logical vector
print(a)
print(b)
print(c)


# In[2]:


#MATRIKS
import numpy as np
cells = [3, 15, -27, 38]
r_nicho = ["R1", "R2"]
c_nicho = ["C1", "C2"]
nicho_matrix = np.matrix(cells).reshape(2, 2)
print(nicho_matrix)


# In[3]:


import pandas as pd
import numpy as np

nicho1 = [1, 2, 3, 4]
nicho2 = ["red", "white", "red", np.nan]  # Menggunakan np.nan untuk merepresentasikan NA
nicho3 = [True, True, True, False]

data_nicho = pd.DataFrame({'ID': nicho1, 'Color': nicho2, 'Passed': nicho3})
print(data_nicho)


# In[4]:


data_nicho = pd.DataFrame({'id': list('abcdefghij'), 'x': list(range(1, 11)), 'y': list(range(11, 21))})
print(data_nicho)


# In[5]:


pip install mysql-connector-python


# In[9]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="houseprices"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM nicho_houseprice;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi

    cursor.close()
    connection.close()


# In[17]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[df['COL 6'] == 'No']

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[18]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[(df['COL 6'] == 'No') | (df['COL 7'] == 'East')]

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[23]:


import mysql.connector

# Membuat koneksi ke MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ps2[nicho]"
)

# Membuat objek cursor untuk mengeksekusi kueri
cursor = connection.cursor()

try:
    # Mengeksekusi kueri SQL
    my_query = "SELECT * FROM d4t4;"
    cursor.execute(my_query)
    
    # Mengambil semua hasil kueri
    result = cursor.fetchall()
    
    # Menampilkan hasil kueri
    print("\nHasil Kueri:")
    for row in result:
        print(row)

finally:
    # Menutup kursor dan koneksi

    cursor.close()
    connection.close()


# In[24]:


import pandas as pd
# Mengonversi hasil kueri ke DataFrame Pandas
df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])

# Filter data berdasarkan kolom 'Brick' yang bernilai 'No'
df_filtered = df[(df['COL 2'] == 'L')]

# Menampilkan hasil filter
print("\nHasil Filter:")
print(df_filtered)


# In[ ]:





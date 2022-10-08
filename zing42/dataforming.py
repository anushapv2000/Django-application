#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install mysql-connector-python==8.0.30 


# In[1]:


import mysql.connector
from mysql.connector import Error
import csv


# In[2]:


import os
import shutil
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup


# In[4]:


url1="https://www.nseindia.com/market-data/securities-available-for-trading"


# In[ ]:


import requests

URL ="https://archives.nseindia.com/content/equities/EQUITY_L.csv"
response = requests.get(URL)


# In[ ]:


open("EQUITY_L.csv", "wb").write(response.content)


# In[ ]:


url2="https://archives.nseindia.com/content/historical/EQUITIES/2022/OCT/cm07OCT2022bhav.csv.zip"


# In[ ]:


response = requests.get(url2)
open("cm07OCT2022bhav.csv", "wb").write(response.content)


# In[ ]:





# In[ ]:





# In[21]:


conn=mysql.connector.connect(host='127.0.0.1',
                                         port='3306',
                                         database='EQUITY_L',
                                         user='root',
                                         password='Sandstone@34')


# In[88]:


with open('C:/Users/anush/Videos/zing42/EQUITY_L.csv') as equity:
    f=csv.reader(equity)
    vals=[]
    for r in f:
        v=(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7])
        vals.append(v)


# In[105]:


b=vals[1:]


# In[23]:


df=pd.read_csv('C:/Users/anush/Videos/zing42/EQUITY_L.csv')


# In[22]:


cursor=conn.cursor()


# In[35]:


df.head()


# In[25]:


df.columns


# In[102]:


cursor.execute("create table equity (`SYMBOL` varchar(150), `NAME_OF_COMPANY`  varchar(150), `SERIES` varchar(150),  `DATE OF LISTING` varchar(50),  `PAID UP VALUE` INT,   `MARKET LOT` int,  `ISIN NUMBER` varchar(150),  `FACE VALUE` int)")


# In[104]:


#for r in df.itertuples():
cursor.executemany('''INSERT INTO equity(`SYMBOL`, `NAME OF COMPANY`, `SERIES`, `DATE OF LISTING`,`PAID UP VALUE`, `MARKET LOT`, `ISIN NUMBER`, `FACE VALUE`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''',b) 
conn.commit()


# In[122]:


with open("C:/Users/anush/Videos/zing42/cm07OCT2022bhav.csv/cm07OCT2022bhav.csv") as cm0:
    f2=csv.reader(cm0)
    vals=[]
    for r in f2:
        v=(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12])
        vals.append(v)


# In[124]:


b=vals[1:]


# In[107]:


df=pd.read_csv('C:/Users/anush/Videos/zing42/cm07OCT2022bhav.csv/cm07OCT2022bhav.csv')


# In[112]:


df.head()


# In[113]:


df.columns


# In[127]:


cursor.execute("create table cm07 (`SYMBOL` varchar(100), `SERIES` varchar(50), `OPEN` float, `HIGH` float, `LOW` float, `CLOSE` float, `LAST` float, `PREVCLOSE` float,`TOTTRDQTY` int, `TOTTRDVAL` float, `TIMESTAMP` varchar(50), `TOTALTRADES` int, `ISIN` varchar(150))")


# In[128]:


cursor.executemany('''INSERT INTO cm07(`SYMBOL`, `SERIES`, `OPEN`, `HIGH`, `LOW`, `CLOSE` , `LAST`, `PREVCLOSE` ,`TOTTRDQTY`, `TOTTRDVAL` , `TIMESTAMP`, `TOTALTRADES`, `ISIN`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',b)


# In[ ]:





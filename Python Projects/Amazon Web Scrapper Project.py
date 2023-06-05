#!/usr/bin/env python
# coding: utf-8

# In[11]:


# import libraries

from bs4 import BeautifulSoup
import requests
import time
import datetime
from os import environ

import smtplib


# In[34]:


# Connect to Website

URL = 'https://www.amazon.sa/-/en/dp/B097G7RBSZ/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A2XPWB6MYN7ZDK&pf_rd_s=merchandised-search-8&pf_rd_r=9DXDJWERW7GNP5KS7Z6G&pf_rd_t=101&pf_rd_p=7e6fa8c3-67a6-4a15-a363-c017ad272233&pf_rd_i=26955031031'

headers = {
    "User-Agent": environ.get("User-Agent"),
    "Accept-Language": environ.get("Accept-Language")
}

page = requests.get(URL, headers= headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
           
title = soup2.find(id = 'productTitle').get_text()

price = soup2.find('span', {'class':'a-offscreen'}).get_text()
        
print(title)
print(price)


# In[38]:


#price = price.strip()[3:]
#title = title.strip()

print(title)
print(price)


# In[ ]:


#importing date

import datetime

datetime.date.today()
print(today)


# In[46]:


import csv

header = ['Title', 'Price', 'Date Imported']
data = [title, price, today]




# In[51]:


#Reading CSV file

import pandas as pd

df = pd.read_csv(r'C:\Users\Ash\Python\AmazonWebScraperDataset.csv')

df


# In[50]:


#Append data in CSV

with open('AmazonWebScraperDataset.csv', 'a+', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[ ]:


def check_price():
    URL = 'https://www.amazon.sa/-/en/dp/B097G7RBSZ/ref=s9_acsd_al_bw_c2_x_0_i?pf_rd_m=A2XPWB6MYN7ZDK&pf_rd_s=merchandised-search-8&pf_rd_r=9DXDJWERW7GNP5KS7Z6G&pf_rd_t=101&pf_rd_p=7e6fa8c3-67a6-4a15-a363-c017ad272233&pf_rd_i=26955031031'

    headers = {
        "User-Agent": environ.get("User-Agent"),
        "Accept-Language": environ.get("Accept-Language")
    }

    page = requests.get(URL, headers= headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
           
    title = soup2.find(id = 'productTitle').get_text()

    price = soup2.find('span', {'class':'a-offscreen'}).get_text()
    
    price = price.strip()[3:]
    title = title.strip()
    
    import datetime
    today = datetime.date.today()
    
    import csv

    header = ['Title', 'Price', 'Date Imported']
    data = [title, price, today]
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline = '', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[55]:


import pandas as pd

df = pd.read_csv(r'C:\Users\Ash\Python\AmazonWebScraperDataset.csv')

df


# In[ ]:





# In[ ]:





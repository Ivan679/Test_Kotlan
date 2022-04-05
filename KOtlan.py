#!/usr/bin/env python
# coding: utf-8

# In[97]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json
 

response = requests.post('https://ies-midterm.soulution.rocks/login', json = {'cuni':'63363541'})

#print(response.json())
#print('personal_code:74c79033')


response2 = requests.get('https://ies-midterm.soulution.rocks/data/81395feb08')
response3 = requests.get('https://ies-midterm.soulution.rocks/data/288b147f95')
response4 = requests.get('https://ies-midterm.soulution.rocks/data/24f88cb68c')
response5 = requests.get('https://ies-midterm.soulution.rocks/data/86c214b421')
response6 = requests.get('https://ies-midterm.soulution.rocks/data/3bd4cabfaa')
response7 = requests.get('https://ies-midterm.soulution.rocks/data/3e8641892a')

#p_jsn= print(response2.json())
#print(response3.json())
#print(response4.json())
#print(response5.json())
#print(response6.json())
#print(response7.json())
strin_pd = pd.read_json(response2, orient = "index")









# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





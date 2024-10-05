#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd 
import seaborn as sns
data = pd.read_csv(r"C:\Users\DELL\Desktop\PYthon portfolio projects\file (1).csv")


# In[6]:


data


# ## Task 1 Finding all duplicates in the data set

# In[7]:


data.head(5)


# In[8]:


data.shape


# In[11]:


data[data.duplicated()]


# In[13]:


data.drop_duplicates(inplace = True)


# ## 2. Is there any  null values in any column? show with heatmap

# In[15]:


data.head()


# In[16]:


data.isnull()


# In[18]:


data.isnull().sum()


# In[19]:


import seaborn as sns


# In[20]:


sns.heatmap(data.isnull())


# ### Q1 - For ' House of cards' what is the show id and who is the director of this show ?

# In[21]:


data.head()


# In[22]:


data[data['Title'].isin(['House of Cards'])]


# ### In which year was the highest number of TV shows and Movies released? show with bar graph

# In[25]:


data.dtypes


# In[45]:


#to_datetime
#data['Release_Date'] = pd.to_datetime(data['Release_Date'], dayfirst=True, errors='coerce')
df = data['Date_N'] = pd.to_datetime(data['Release_Date'], dayfirst=True, errors='coerce')


# In[46]:


data.head()


# In[32]:


data['Date_N'].dt.year.value_counts()


# In[33]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# ### how many Movies and TV shows are in the dataset? show with Bar Graph

# In[35]:


data.head(2)


# In[37]:


data.groupby('Category').Category.count()


# In[40]:


sns.countplot(x = 'Category', data=data)


# ### show all the movies that were released in the year 2000

# In[51]:


#create a  new column that contains only the year
data['Year'] = data['Date_N'].dt.year


# In[52]:


data.head(2)


# In[58]:


data [(data['Category'] == 'Movie') & (data['Year']==2000)]


# ### show only the title of all tv shows that were release in india only 

# In[59]:


data.head(2)


# In[62]:


data [(data['Category']=='TV Show') & (data['Country']=='India')] ['Title']


# ### show Top 10 directors, who gave the highest number of Tv shows and movies to Neltflix

# In[63]:


data.head(2)


# In[65]:


data['Director'].value_counts().head(10)


# ### show all the records where "category is movies and type is comedies or cuntry is United Kingdom

# In[66]:


data.head(2)


# In[69]:


data [(data['Category'] =='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# ### In how many and shows is Tom Cruise in the cast

# In[70]:


data.head(2)


# In[72]:


data [(data['Cast']=='Tom Cruise')]


# In[74]:


data [(data['Cast'].str.contains('Tom Cruise'))]


# In[75]:


data_new = data.dropna()


# In[76]:


data_new.head(2)


# In[77]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ### What are the different ratings defined by netflix

# In[78]:


data.head(2)


# In[79]:


data['Rating'].nunique()


# ### How many movies git the Tv-14 Rating in canada

# In[82]:


data[(data['Category']== 'Movie') & (data['Rating']=='TV-14')]


# In[87]:


data[(data['Category']== 'Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape


# ### How many tv shows got the R rating after year 2018?
# 

# In[88]:


data.head(2)


# In[97]:


data[(data['Category']=='TV show') & (data['Rating']=='R') & (data['Year'] > 2018)]


# ### What is the maximum duration of a movie/tv show on Netflix

# In[98]:


data.head(2)


# In[100]:


data.Duration.unique()


# In[101]:


data[['Min', 'Unit']] = data['Duration'].str.split(' ', expand=True)


# In[102]:


data.head(2)


# In[104]:


data['Min'].max()


# ### Which individual country has the highest  No. of Tv SHOWS 

# In[105]:


data.head(2)


# In[108]:


data_tvshow = data[data['Category']== 'TV Show']


# In[109]:


data_tvshow.head(2)


# In[110]:


data_tvshow.Country.value_counts()


# In[111]:


data_tvshow.Country.value_counts().head(1)


# ### How can we sort the dataset by year

# In[112]:


data.head(2)


# In[113]:


data.sort_values(by = 'Year')


# ### Find all instances where 
# 
# ## Category is Movie and Type is Dramas
# 
# ### or Category is TV show and type is kids TV

# In[114]:


data.head(2)


# In[116]:


data[(data['Category']=='Movie') & (data['Type']=='Dramas')].head(2)


# In[119]:


data[(data['Category']=='TV Show') & (data['Type']=="Kids'TV")]


# In[120]:


data[(data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']=="Kids'TV")] 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





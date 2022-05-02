#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json 
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[2]:


file_dir = 'C:/Users/14153/UCDavis_Code/Bootcamp/ETL/Kaggle/'


# In[3]:


kaggle_metadata = pd.read_csv(f'{file_dir}movies_metadata.csv', low_memory=False)
ratings = pd.read_csv(f'{file_dir}ratings.csv')


# In[4]:


kaggle_metadata.head(5)


# In[5]:


kaggle_metadata.sample(n=5)


# In[6]:


kaggle_metadata.tail(5)


# In[7]:


ratings.head(5)


# In[8]:


ratings.sample(5)


# In[9]:


ratings.tail(5)


# ## 8.3.1 Data Cleaning Strategies

# In[10]:


with open(f'{file_dir}wikipedia_movies.json', mode='r') as file:
    wiki_movies_raw = json.load(file)


# In[11]:


len(wiki_movies_raw)


# In[12]:


wiki_movies_raw[:5]


# In[13]:


wiki_movies_raw[-5:]


# In[14]:


wiki_movies_raw[3600:3605]


# In[15]:


wiki_movies_df = pd.DataFrame(wiki_movies_raw)
wiki_movies_df.head(5)


# In[16]:


columns_list = wiki_movies_df.columns.tolist()
columns_list 


# In[17]:


###List Comprehension to Filter to only the movies wtih a director and IMBD link 
wiki_movies = [movie for movie in wiki_movies_raw
               if ('Director' in movie or 'Directed by' in movie)
                   and 'imdb_link' in movie]
len(wiki_movies)


# ## 8.3.5 Create a Function to Clean Data 

# In[18]:


wiki_movies = [movie for movie in wiki_movies_raw
               if ('Director' in movie or 'Directed by' in movie)
                   and 'imdb_link' in movie
                   and 'No. of episodes' not in movie]


# In[19]:


def clean_movie(movie):
    movie = dict(movie) #create a non-destructive copy
    return movie


# In[20]:


wiki_movies_df[wiki_movies_df['Arabic'].notnull()]


# In[21]:


wiki_movies_df[wiki_movies_df['Arabic'].notnull()]['url']


# In[22]:


sorted(wiki_movies_df.columns.tolist())


# In[23]:


def clean_movie(movie):
    movie = dict(movie) #create a non-destructive copy
    alt_titles = {}
    return movie


# In[36]:


def clean_movie(movie):
    movie = dict(movie) #create a non-destructive copy
    alt_titles = {}
    for key in ['Also known as','Arabic','Cantonese','Chinese','French',
                'Hangul','Hebrew','Hepburn','Japanese','Literally',
                'Mandarin','McCune–Reischauer','Original title','Polish',
                'Revised Romanization','Romanized','Russian',
                'Simplified','Traditional','Yiddish']:

            return movie


# In[38]:


def clean_movie(movie):
    movie = dict(movie) #create a non-destructive copy
    alt_titles = {}
    for key in ['Also known as','Arabic','Cantonese','Chinese','French',
                'Hangul','Hebrew','Hepburn','Japanese','Literally',
                'Mandarin','McCune–Reischauer','Original title','Polish',
                'Revised Romanization','Romanized','Russian',
                'Simplified','Traditional','Yiddish']:
        if key in movie:

            return movie


# In[39]:


def clean_movie(movie):
    movie = dict(movie) #create a non-destructive copy
    alt_titles = {}
    for key in ['Also known as','Arabic','Cantonese','Chinese','French',
                'Hangul','Hebrew','Hepburn','Japanese','Literally',
                'Mandarin','McCune–Reischauer','Original title','Polish',
                'Revised Romanization','Romanized','Russian',
                'Simplified','Traditional','Yiddish']:
        if key in movie:
            alt_titles[key] = movie[key]
            movie.pop(key)


    return movie


# In[40]:


def clean_movie(movie):
    movie = dict(movie) #create a non-destructive copy
    alt_titles = {}
    for key in ['Also known as','Arabic','Cantonese','Chinese','French',
                'Hangul','Hebrew','Hepburn','Japanese','Literally',
                'Mandarin','McCune–Reischauer','Original title','Polish',
                'Revised Romanization','Romanized','Russian',
                'Simplified','Traditional','Yiddish']:
        if key in movie:
            alt_titles[key] = movie[key]
            movie.pop(key)
    if len(alt_titles) > 0:
        movie['alt_titles'] = alt_titles

    return movie


# In[41]:


clean_movies = [clean_movie(movie) for movie in wiki_movies]


# In[42]:


wiki_movies_df = pd.DataFrame(clean_movies)
sorted(wiki_movies_df.columns.tolist())


# In[ ]:





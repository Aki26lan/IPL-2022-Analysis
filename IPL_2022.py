#!/usr/bin/env python
# coding: utf-8

# # IPL 2022 Analysis

# Import required libraries

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Reading the CSV file

# In[2]:


df = pd.read_csv("Downloads/archive (11)/IPL 2022.csv")


# ### 1.Understanding the Data

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.describe()


# ### 2.Cleaning the Data

# In[8]:


df.isnull().sum()


# In[9]:


df.duplicated()


# ### 3.Visual Analysis 

# In[10]:


figure = px.bar(df, x=df["match_winner"],
            title="Number of Matches Won in IPL 2022")
figure.show()


# So, currently, Gujrat is leading the tournament by winning eight matches. It is an achievement as a new team for Gujrat in IPL. 
# Now let’s see how most of the teams win. Here we will analyze whether most of the teams win by defending (batting first) or chasing (batting second)

# In[11]:


figure = px.bar(df, x=df["top_scorer"],
            title="Top Scorers in IPL 2022")
figure.show()


# Currently, Jos Buttler has been a top scorer in 5 matches. He is looking in great touch. 
# Let’s analyze it deeply by including the runs scored by the top scorers

# In[12]:


figure = px.bar(df, x=df["top_scorer"], 
                y = df["highscore"], 
                color = df["highscore"],
            title="Top Scorers in IPL 2022")
figure.show()


# So till now, Jos Buttler has scored three centuries, and KL Rahul has scored two centuries.
# Now let’s have a look at the most player of the match awards till now in IPL 2022

# In[13]:


figure = px.bar(df, x = df["player_of_the_match"], 
                title="Most Player of the Match Awards")
figure.show()


# So Kuldeep Yadav is leading in the list of players of the match awards with four matches. It is a great tournament for Kuldeep Yadav this year.
# Now let’s have a look at the bowlers with the best bowling figures in most of the matches

# In[14]:


figure = px.bar(df, x=df["best_bowling"],
            title="Best Bowlers in IPL 2022")
figure.show()


# You can see Yuzvendra Chahal having the best bowling figures in four matches. So this is a great tournament for Yuzvendra Chahal this year too.
# Now let’s have a look at whether most of the wickets fall while setting the target or while chasing the target

# In[15]:


figure = go.Figure()
figure.add_trace(go.Bar(
    x=df["venue"],
    y=df["first_ings_wkts"],
    name='First Innings Wickets',
    marker_color='gold'
))
figure.add_trace(go.Bar(
    x=df["venue"],
    y=df["second_ings_wkts"],
    name='Second Innings Wickets',
    marker_color='lightgreen'
))
figure.update_layout(barmode='group', xaxis_tickangle=-45)
figure.show()


# So in the Wankhede Stadium in Mumbai and MCA Stadium in Pune, most wickets fall while chasing the target. And in the other two stadiums, most wickets fall while setting the target.
# 
# So this is how you can analyze and summarize the story of IPL 2022 using Python
# 

# =====================================================================================================================================================
# So this is how you can perform the task of IPL 2022 analysis using Python. IPL 2022 is going great for Gujrat as a new team this year. 
# Jos Buttler and KL Rahul have been great with the bat, and Yuzvendra Chahal and Kuldeep Yadav have been great with the bowl

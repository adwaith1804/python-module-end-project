#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('C:/Users/dambd/Downloads/myexcel - myexcel.csv.csv')
 # Use the correct file path
df


# In[10]:


df['Height'].isna().sum()  # Check for missing values
df['Height'].describe()    # Check for any outliers or invalid data


# In[12]:


df['Height']


# In[16]:


df['Height'] = pd.to_numeric(df['Height'], errors='coerce')

# Apply the transformation
df['Height'] = df['Height'].apply(
    lambda x: np.random.randint(150, 181) if pd.isnull(x) or x < 150 or x > 180 else x)


# In[17]:


df


# In[19]:


df['Height'].describe()


# In[21]:


team_distribution = df['Team'].value_counts(normalize=True) * 100
print(team_distribution)


# In[22]:


team_distribution.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title="Employee Distribution Across Teams")
plt.show()


# In[23]:


position_count = df['Position'].value_counts()
print(position_count)


# In[24]:


position_count.plot(kind='bar', figsize=(10, 6), title="Employees by Position")
plt.xlabel("Position")
plt.ylabel("Number of Employees")
plt.show()


# In[26]:


bins = [20, 30, 40, 50, 60]  # Define age groups
labels = ['20-30', '30-40', '40-50', '50-60']
df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

age_group_count = df['age_group'].value_counts()
print(age_group_count)


# In[27]:


age_group_count.plot(kind='bar', figsize=(8, 6), title="Predominant Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")
plt.show()


# In[29]:


salary_by_team_position = df.groupby(['Team', 'Position'])['Salary'].sum()
highest_salary = salary_by_team_position.idxmax(), salary_by_team_position.max()
print(f"Highest Salary Expenditure: {highest_salary}")


# In[30]:


salary_by_team_position.unstack().plot(kind='bar', stacked=True, figsize=(10, 6), title="Salary Expenditure by Team and Position")
plt.ylabel("Salary")
plt.show()


# In[31]:


correlation = df['Age'].corr(df['Salary'])
print(f"Correlation between Age and Salary: {correlation}")


# In[33]:


plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title("Correlation between Age and Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()


# In[ ]:





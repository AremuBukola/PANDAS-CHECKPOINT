#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
exam_data = {"Name":['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        "Score":[12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        "attempts":[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        "qualify":['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print(df)


# In[2]:


# Print the first three rows using head()
print(df.head(3))


# In[3]:


# Drop rows with NaN values
df_cleaned = df.dropna()
print(df_cleaned)


# In[11]:


exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
# Create DataFrame
df = pd.DataFrame(exam_data, index=labels)
selected_columns=df.loc[:,['name', 'score']]
print(selected_columns)


# In[12]:


# Append a new row 'k' with specified values
new_row_data = {'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}
df = df.append(pd.Series(new_row_data, name='k'))

# Display the DataFrame after appending the new row
print(df)


# In[13]:


# Delete the 'attempts' column
df = df.drop('attempts', axis=1)

# Display the DataFrame after deleting the 'attempts' column
print(df)


# In[14]:


# Add a new column "Success"
df['Success'] = np.where(df['score'] > 10, 1, 0)

# Display the DataFrame with the new "Success" column
print(df)


# In[16]:


# Export the DataFrame to a CSV file
df.to_csv('my_data.csv', index=False)


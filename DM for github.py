#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_co2 = pd.read_csv(r"C:\Users\User\Downloads\annual-co2-emissions-per-country.csv")
df_gdp = pd.read_excel(r"C:\Users\User\Downloads\imf-dm-export-20251209.xls")

df_co2.head()


# In[76]:


df_co2 = df_co2.pivot_table(index=['Entity', 'Code'], columns='Year', values='co2')
df_co2 = df_co2.reset_index()
df_co2.head()


# In[77]:


df_co2 = df_co2[['Entity', 'Code', 2003,2023]]
df_co2.columns.name = None
print(df_co2.head())


# In[78]:


df_gdp[2023] = pd.to_numeric(df_gdp[2023], errors='coerce')
df_gdp = df_gdp.sort_values(by=2023, ascending=False)
df_gdp.head()


# In[88]:


top_20 = [
    'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'Spain', 'France', 
    'United Kingdom', 'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 
    'Mexico', 'Netherlands', 'Russia', 'Saudi Arabia', 'Switzerland', 'Turkey', 
    'United States'
]

 
df_gdp = df_gdp[df_gdp['Country'].isin(top_20)]



# In[80]:


df_gdp = df_gdp[["Country",2003,2023]]
df_gdp = df_gdp.reset_index(drop=True)
df_gdp.head()


# In[83]:


plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
ax = sns.barplot(data=df_gdp, x='Country', y=2023, palette='viridis')


plt.title('2023 GDP Ranking top 20 Countries', fontsize=16, fontweight='bold')
plt.xlabel('Countries', fontsize=12)
plt.ylabel('Gross Domestic Product (Billion USD)', fontsize=12)


plt.xticks(rotation=45, ha='right')

for i in ax.containers:
    ax.bar_label(i, fmt='%.0f', padding=3, fontsize=9)


plt.tight_layout()
plt.show()


# In[84]:


import matplotlib.pyplot as plt


df_gdp.plot(x='Country', y=[2003, 2023], kind='bar', figsize=(15, 8), width=0.8, colormap='viridis')

plt.title('2003 vs 2023 GDP Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Countries', fontsize=12)
plt.ylabel('GDP (Billion USD)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()


# In[85]:


import matplotlib.pyplot as plt


plt.figure(figsize=(15, 8))


plt.plot(df_gdp['Country'], df_gdp[2003], marker='o', label='2003', linewidth=2)
plt.plot(df_gdp['Country'], df_gdp[2023], marker='o', label='2023', linewidth=2)


plt.title('GDP Comparison: 2003 vs 2023', fontsize=16, fontweight='bold')
plt.xlabel('Countries', fontsize=12)
plt.ylabel('GDP (Billion USD)', fontsize=12)


plt.xticks(rotation=45, ha='right')

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Year', fontsize=11)


plt.tight_layout()
plt.show()


# In[87]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_long = df_gdp.melt(id_vars='Country', value_vars=[2003, 2023], 
                      var_name='Year', value_name='GDP')


plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")


sns.lineplot(data=df_long, x='Year', y='GDP', hue='Country', 
             marker='o', palette='tab20', linewidth=2.5)


plt.title('GDP Evolution of Countries (2003 - 2023)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('GDP (Billion USD)', fontsize=12)


plt.xticks([2003, 2023])


plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, title='Country')

plt.tight_layout()
plt.show()


# In[91]:


df_co2 = df_co2[df_co2['Entity'].isin(top_20)]
df_co2 = df_co2.reset_index(drop=True)

df_co2.head()


# In[106]:


import matplotlib.pyplot as plt
import seaborn as sns


df_plot = df_co2.melt(id_vars=['Entity', 'Code'], 
                      value_vars=[2003, 2023], 
                      var_name='Year', 
                      value_name='Value')


plt.figure(figsize=(10, 6))

ax = sns.barplot(data=df_plot, x='Entity', y='Value', hue='Year', palette='viridis')

plt.title('Comparison by Country: 2003 vs 2023', fontsize=14) 
plt.xlabel('Country', fontsize=12)  
plt.ylabel('Value', fontsize=12)   
plt.grid(axis='y', linestyle='--', alpha=0.5)


plt.xticks(rotation=45) 

plt.tight_layout() 
plt.show()


# In[107]:


import matplotlib.pyplot as plt
import seaborn as sns


df_plot = df_co2.melt(id_vars=['Entity', 'Code'], 
                      value_vars=[2003, 2023], 
                      var_name='Year', 
                      value_name='Value')

df_plot['Year'] = df_plot['Year'].astype(str) 


plt.figure(figsize=(10, 6))


sns.lineplot(data=df_plot, x='Entity', y='Value', hue='Year', marker='o', palette='viridis')


plt.title('Comparison by Country: 2003 vs 2023', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5) 


plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# In[108]:


import matplotlib.pyplot as plt
import seaborn as sns


df_plot = df_co2.melt(id_vars=['Entity', 'Code'], 
                      value_vars=[2003, 2023], 
                      var_name='Year', 
                      value_name='Value')


df_plot['Year'] = df_plot['Year'].astype(str)


plt.figure(figsize=(10, 6))


sns.lineplot(data=df_plot, x='Year', y='Value', hue='Entity', marker='o', palette='bright', linewidth=2.5)


plt.title('Change in Value: 2003 to 2023', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)


plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Country')

plt.tight_layout() 
plt.show()


# In[111]:


df_co2.head()


# In[112]:


df_gdp.head()


# In[123]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.close('all') 



gdp_safe = df_gdp.melt(id_vars=['Country'], value_vars=[2003, 2023], 
                       var_name='Year', value_name='GDP').copy()
gdp_safe['GDP'] = gdp_safe['GDP'] / 1000 



co2_safe = df_co2.rename(columns={'Entity': 'Country'}).melt(
                       id_vars=['Country', 'Code'], value_vars=[2003, 2023], 
                       var_name='Year', value_name='CO2').copy()
co2_safe['CO2'] = co2_safe['CO2'] / 1_000_000_000


df_plot = pd.merge(gdp_safe, co2_safe, on=['Country', 'Year'])


plt.figure(figsize=(12, 7))


sns.lineplot(data=df_plot, x='GDP', y='CO2', hue='Country', 
             sort=False, lw=2, palette='tab10', legend=False, alpha=0.6)


sns.scatterplot(data=df_plot, x='GDP', y='CO2', hue='Country', 
                style='Year', s=150, palette='tab10', edgecolor='black')


plt.title('GDP vs CO2 Emissions (2003 - 2023 Trends)', fontsize=16)
plt.xlabel('GDP (Trillion USD)', fontsize=12)
plt.ylabel('CO2 Emissions (Billion Tonnes)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)


plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', title='Country / Year', borderaxespad=0.)

plt.tight_layout()
plt.show()


# In[124]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.close('all')


exclude = ['United States', 'China', 'USA', 'CHN']



gdp_data = df_gdp[~df_gdp['Country'].isin(exclude)].melt(
    id_vars=['Country'], value_vars=[2003, 2023], 
    var_name='Year', value_name='GDP').copy()

gdp_data['GDP'] = gdp_data['GDP'] / 1000 # Milyar -> Trilyon


co2_data = df_co2[~df_co2['Entity'].isin(exclude)].rename(
    columns={'Entity': 'Country'}).melt(
    id_vars=['Country', 'Code'], value_vars=[2003, 2023], 
    var_name='Year', value_name='CO2').copy()

co2_data['CO2'] = co2_data['CO2'] / 1_000_000_000 # Sayı -> Milyar Ton


df_plot = pd.merge(gdp_data, co2_data, on=['Country', 'Year'])


plt.figure(figsize=(12, 7))


sns.lineplot(data=df_plot, x='GDP', y='CO2', hue='Country', 
             sort=False, lw=2, palette='tab10', legend=False, alpha=0.6)


sns.scatterplot(data=df_plot, x='GDP', y='CO2', hue='Country', 
                style='Year', s=150, palette='tab10', edgecolor='black')

plt.title('GDP vs CO2 Emissions (2003 - 2023 Trends)\nExcluding US & China', fontsize=15)
plt.xlabel('GDP (Trillion USD)', fontsize=12)
plt.ylabel('CO2 Emissions (Billion Tonnes)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)


plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', title='Country / Year')

plt.tight_layout()
plt.show()


# In[128]:


import plotly.express as px
import pandas as pd


top_20 = [
    'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'Spain', 'France', 
    'United Kingdom', 'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 
    'Mexico', 'Netherlands', 'Russia', 'Saudi Arabia', 'Switzerland', 'Turkey', 
    'United States'
]


df_map = pd.DataFrame({
    'Country': top_20,
    'Value': [1] * len(top_20)  # Hepsine 1 veriyoruz (Hepsi aynı renk olsun diye)
})


fig = px.choropleth(df_map,
                    locations="Country",        
                    locationmode="country names",
                    color="Value",              
                    hover_name="Country",       
                    color_continuous_scale="Blues",  
                    projection="natural earth",  
                    title="Analysis Scope: Top 20 Countries"
                    )


fig.update_layout(coloraxis_showscale=False)


fig.show()


# In[ ]:





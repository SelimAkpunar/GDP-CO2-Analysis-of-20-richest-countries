#!/usr/bin/env python
# coding: utf-8

# # reading the dataset

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_co2 = pd.read_csv(r"C:\Users\User\Desktop\Data Visualization\GDP-CO2\annual-co2-emissions-per-country.csv")
df_gdp = pd.read_excel(r"C:\Users\User\Desktop\Data Visualization\GDP-CO2\imf-dm-export-20251209.xls")

df_co2.head()


# # pivoting the dataset from long to wide

# In[4]:


df_co2 = df_co2.pivot_table(index=['Entity', 'Code'], columns='Year', values='co2')
df_co2 = df_co2.reset_index()
df_co2.head()


# # deleting all years outside 2003 and 2023

# In[5]:


df_co2 = df_co2[['Entity', 'Code', 2003,2023]]
df_co2.columns.name = None
print(df_co2.head())


# # ordering according to 2023 values

# In[6]:


df_gdp[2023] = pd.to_numeric(df_gdp[2023], errors='coerce')
df_gdp = df_gdp.sort_values(by=2023, ascending=False)
df_gdp.head()


# # choosing the top 20 countries

# In[7]:


top_20 = [
    'Australia', 'Brazil', 'Canada', 'China', 'Germany', 'Spain', 'France', 
    'United Kingdom', 'Indonesia', 'India', 'Italy', 'Japan', 'South Korea', 
    'Mexico', 'Netherlands', 'Russia', 'Saudi Arabia', 'Switzerland', 'Turkey', 
    'United States'
]

 
df_gdp = df_gdp[df_gdp['Country'].isin(top_20)]



# # deleting all years outside 2003 and 2023

# In[8]:


df_gdp = df_gdp[["Country",2003,2023]]
df_gdp = df_gdp.reset_index(drop=True)
df_gdp.head()


# # plotting graphs for different relationships

# In[32]:


plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
ax = sns.barplot(data=df_gdp, x='Country', y=2023, palette='viridis')


plt.title('2023 GDP Ranking top 20 Countries', fontsize=16, fontweight='bold')
plt.xlabel('Countries', fontsize=12)
plt.ylabel('Gross Domestic Product (Billion USD)', fontsize=12)


plt.xticks(rotation=90, ha='right')

for i in ax.containers:
    ax.bar_label(i, fmt='%.0f', padding=3, fontsize=9)


plt.tight_layout()
plt.show()


# In[33]:


import matplotlib.pyplot as plt


df_gdp.plot(x='Country', y=[2003, 2023], kind='bar', figsize=(15, 8), width=0.8, colormap='viridis')

plt.title('2003 vs 2023 GDP Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Countries', fontsize=12)
plt.ylabel('GDP (Billion USD)', fontsize=12)
plt.xticks(rotation=90, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()


# In[11]:


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


# In[12]:


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


# In[13]:


df_co2 = df_co2[df_co2['Entity'].isin(top_20)]
df_co2 = df_co2.reset_index(drop=True)

df_co2.head()


# In[14]:


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


# In[15]:


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


# In[16]:


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


# In[17]:


df_co2.head()


# In[18]:


df_gdp.head()


# In[19]:


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


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.close('all')


exclude = ['United States', 'China', 'USA', 'CHN']



gdp_data = df_gdp[~df_gdp['Country'].isin(exclude)].melt(
    id_vars=['Country'], value_vars=[2003, 2023], 
    var_name='Year', value_name='GDP').copy()

gdp_data['GDP'] = gdp_data['GDP'] / 1000  


co2_data = df_co2[~df_co2['Entity'].isin(exclude)].rename(
    columns={'Entity': 'Country'}).melt(
    id_vars=['Country', 'Code'], value_vars=[2003, 2023], 
    var_name='Year', value_name='CO2').copy()

co2_data['CO2'] = co2_data['CO2'] / 1_000_000_000  


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


# In[26]:


import pandas as pd
import plotly.express as px

df_co2_melted = df_co2.melt(id_vars=['Entity', 'Code'], var_name='Year', value_name='Amount_CO2')
df_gdp_melted = df_gdp.melt(id_vars=['Country'], var_name='Year', value_name='GDP')

df_co2_melted['Year'] = df_co2_melted['Year'].astype(int)
df_gdp_melted['Year'] = df_gdp_melted['Year'].astype(int)

df_merged = pd.merge(df_co2_melted, df_gdp_melted, left_on=['Entity', 'Year'], right_on=['Country', 'Year'])

df_merged['Amount_CO2_Million'] = df_merged['Amount_CO2'] / 1000000

target_years = [2003, 2023]
df_plot = df_merged[df_merged['Year'].isin(target_years)].copy()
to_exclude = ['USA', 'CHN']
df_plot = df_plot[~df_plot['Code'].isin(to_exclude)]

top_6_codes = df_plot[df_plot['Year'] == 2023].nlargest(4, 'Amount_CO2_Million')['Code'].tolist()

country_list = df_plot['Code'].unique()
color_map = {country: 'lightgrey' for country in country_list}

highlight_colors = px.colors.qualitative.Plotly
for i, code in enumerate(top_6_codes):
    color_map[code] = highlight_colors[i]

fig = px.line(
    df_plot,
    x='GDP',
    y='Amount_CO2_Million',
    color='Code',
    color_discrete_map=color_map,
    markers=True,
    title='GDP vs CO₂ Emission: Top 4 Emitters (Excluding USA & China)',
    labels={
        'Amount_CO2_Million': 'CO₂ Emissions (Million Metric Tons)',
        'GDP': 'GDP (Billions of US Dollar)',
        'Code': 'Country'
    },
    template='plotly_white'
)

fig.update_traces(line=dict(width=1))
for code in top_6_codes:
    fig.update_traces(selector=dict(name=code), line=dict(width=4))

fig.update_layout(
    yaxis=dict(
        tickformat='d',
        dtick=500,
        gridcolor='#E5E5E5'
    ),
    xaxis=dict(gridcolor='#E5E5E5'),
    showlegend=True
)

fig.show()


# In[30]:


import pandas as pd
import plotly.express as px

# --- Sizin paylaştığınız veri hazırlama kısmı ---
df_co2_melted = df_co2.melt(id_vars=['Entity', 'Code'], var_name='Year', value_name='Amount_CO2')
df_gdp_melted = df_gdp.melt(id_vars=['Country'], var_name='Year', value_name='GDP')

df_co2_melted['Year'] = df_co2_melted['Year'].astype(int)
df_gdp_melted['Year'] = df_gdp_melted['Year'].astype(int)

df_merged = pd.merge(df_co2_melted, df_gdp_melted, left_on=['Entity', 'Year'], right_on=['Country', 'Year'])
df_merged['Amount_CO2_Million'] = df_merged['Amount_CO2'] / 1000000

target_years = [2003, 2023]
df_plot = df_merged[df_merged['Year'].isin(target_years)].copy()
to_exclude = ['USA', 'CHN']
df_plot = df_plot[~df_plot['Code'].isin(to_exclude)]

# --- Yeni Mantık: Gidişat Analizi (Hocanın istediği 3 ana grup) ---

# 1. 2003-2023 değişimini hesapla
df_diff = df_plot.pivot(index='Code', columns='Year', values='Amount_CO2_Million')
df_diff['Change'] = df_diff[2023] - df_diff[2003]

# 2. Ülkeleri kategorilere göre seç
rising_country = df_diff['Change'].idxmax()          # En çok artan (Aşırı Artış)
falling_country = df_diff['Change'].idxmin()         # En çok azalan (Ayrışma/Decoupling)
flat_country = df_diff['Change'].abs().idxmin()      # Farkı sıfıra en yakın olan (Yatay)

highlights = {
    rising_country: 'red',    # Artanlar için kırmızı
    falling_country: 'green', # Azalanlar için yeşil
    flat_country: 'blue'      # Sabitler için mavi
}

# 3. Renk Haritasını Oluştur
country_list = df_plot['Code'].unique()
color_map = {country: 'lightgrey' for country in country_list}
for code, color in highlights.items():
    color_map[code] = color

# 4. Grafiği Çiz
fig = px.line(
    df_plot,
    x='GDP',
    y='Amount_CO2_Million',
    color='Code',
    color_discrete_map=color_map,
    markers=True,
    title='Comparison of Trajectories (2003-2023): Rising, Falling, and Flat Emitters',
    labels={
        'Amount_CO2_Million': 'CO₂ Emissions (Million Metric Tons)',
        'GDP': 'GDP (Billions of US Dollar)',
        'Code': 'Country'
    },
    template='plotly_white'
)

# 5. Görsel Hiyerarşi
fig.update_traces(line=dict(width=1), opacity=1) # Diğerleri ince ve şeffaf
for code in highlights.keys():
    fig.update_traces(selector=dict(name=code), line=dict(width=5), opacity=1)

fig.update_layout(
    yaxis=dict(tickformat='d', gridcolor='#E5E5E5'),
    xaxis=dict(gridcolor='#E5E5E5'),
    showlegend=True
)

fig.show()


# # showing the 20 countries that has been used

# In[24]:


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


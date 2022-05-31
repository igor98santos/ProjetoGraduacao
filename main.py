import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify as sq
import seaborn as sns
import statsmodels.formula.api as smf
import csv

with open('top50.csv', 'r') as entrada:
    ler = csv.reader(entrada)

filename='top50.csv'
data=pd.read_csv(filename,encoding='ISO-8859-1')
data.rename(columns={'Unnamed: 0':'ID','Track.Name':'track_name','Artist.Name':'artist_name','Beats.Per.Minute':'beats_per_minute','Loudness..dB..':'Loudness(dB)','Valence.':'Valence','Length.':'Length', 'Acousticness..':'Acousticness','Speechiness.':'Speechiness'},inplace=True)
data.isnull().sum()
data.fillna(0)

print(type(data['artist_name']))
popular_artist=data.groupby('artist_name').size().unique
print(popular_artist)
artist_list=data['artist_name'].values.tolist()


# grafico 1
plt.figure(figsize=(14,8))
plt.title('Artistas no Spotify Top 50 faixas 2019', fontsize = 20)
sq.plot(data.artist_name.value_counts().values, label=data.artist_name.value_counts().index, alpha=.8)
plt.axis('off')
plt.show()

#Grafico 2
x = ['atl hip hop', 'australian pop', 'big room', 'boy band', 'brostep',
'canadian hip hop', 'canadian pop', 'country rap', 'dance pop', 'dfw rap',
'edm', 'electropop', 'escape room', 'latin', 'panamanian pop',
'pop', 'pop house', 'r&b en espanol', 'reggaeton', 'reggaeton flow',
'trap music']
genre_groupby = data.groupby('Genre')['track_name'].agg(len)
plt.figure(figsize = (25,8))
plt.xticks(rotation = 40, fontsize = 13)
plt.ylabel('Tracks Number', fontsize = 15)
plt.title('Tracks Number Of Different Genres', fontsize = 20)
plt.bar(x,genre_groupby,facecolor = 'yellowgreen',alpha=0.7, edgecolor = 'white',lw=5,label='Genre',width = 0.7)
plt.legend(loc="upper right", fontsize = 20)
plt.show()

#Grafico 3
h=sns.jointplot(x=data["Liveness"].values, y=data['Popularity'].values, height=10, kind="kde",shade=True)
plt.title('Dependence Between Liveness And Popularity', fontsize = 20, loc ='left')
h.set_axis_labels('Liveness', 'Popularity', fontsize=12)
plt.tight_layout()
plt.show()
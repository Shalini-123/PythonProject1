import pandas as pd; 

import matplotlib.pyplot as plt;

#print("----------coffee-survey-results------------")
survey=pd.read_csv('c:\\Users\\Shalini\\Documents\\PY_VSCode\\test\\coffee-survey-results.csv')
#print(survey)
needed_columns = [
    "What kind of dairy? (Whole milk)",
    "What kind of dairy? (Skim milk)",
    "What kind of dairy? (Half and half)",
    "What kind of dairy? (Coffee creamer)",
    "What kind of dairy? (Flavored creamer)",
    "What kind of dairy? (Oat milk)",
    "What kind of dairy? (Almond milk)",
    "What kind of dairy? (Soy milk)"
]
dairy = survey[needed_columns]
print(dairy)

name_map={
    'What kind of dairy? (Whole milk)': 'Whole milk',
    'What kind of dairy? (Skim milk)': 'Skim milk',
    'What kind of dairy? (Half and half)': 'Half and half',
    'What kind of dairy? (Coffee creamer)': 'Coffee creamer',
    'What kind of dairy? (Flavored creamer)': 'Flavored creamer',
    'What kind of dairy? (Oat milk)': 'Oat milk',
    'What kind of dairy? (Almond milk)': 'Almond milk',
    'What kind of dairy? (Soy milk)': 'Soy milk',
}
dairy=dairy.rename(columns=name_map)
print(dairy)

print(dairy.isna().sum())
dairy=dairy.dropna()
dairy_pre= dairy.mean() *100
print(dairy_pre)
dairy_pre=dairy_pre.sort_values()
print(dairy_pre)
#print (dairy.iloc[:, [1,2]])

plt.barh(dairy_pre.index,dairy_pre)
plt.xlabel('Percentage')
plt.show()




#print("----------top-song-durations------------")
#top=pd.read_csv("c:\\Users\\Shalini\\Documents\\PY_VSCode\\test\\top-song-durations.csv")
#print(top.query('duration == duration.min()'))
#plt.plot(top['year'],top['duration'])
#print(top.info())#
#print(top)
#top_duration=top['duration'].str.split(':',expand=True)
#print(top_duration)
#top[['h','m','s']]=top_duration.astype('int')
#print(top)
#top['total_sec']=top.eval('h*3600 + m*60 + s')
#print(top)
#plt.plot(top['year'],top['total_sec'])
#plt.xlabel('Year')
#plt.ylabel('Duration (seconds)')
#plt.show()

#print('---fruit-weights.csv---'+'\n\n\n')
#fr= pd.read_csv("c:\\Users\\Shalini\\Documents\\PY_VSCode\\test\\fruit-weights.csv")
#print(fr)
#print('------groups------')
#grp = fr.groupby('fruit')
#sr = grp['weight'].mean()
#print(grp['weight'].mean().reset_index())
#print(sr.reset_index())

#print('---right-triangles---'+'\n\n\n')
#tr= pd.read_csv("c:\\Users\\Shalini\\Documents\\PY_VSCode\\test\\right-triangles.csv")
#tr['area'] = tr.eval('0.5 * base * height')
#print(tr)
#print(tr['area'].mean())
#print(tr.query('area < area.mean()'))


#df=pd.DataFrame()
#df['color'] = ['blue','red','yellow','green']
#df['radius'] = [2,4,3,5]
#df['diameter'] = df['radius']*2

#print(df['radius'].mean())

#print(df['color'])
#print(df)
#print(df.iloc[-1])
#print('---columns---'+'\n')
#print(df.shape[1])

#print('---earth-layers---'+'\n\n\n')

#layers= pd.read_csv("c:\\Users\\Shalini\\Documents\\PY_VSCode\\test\\earth-layers.csv")

#print(layers)
#print(layers['thickness'].mean())

#x = layers['layer']
#y = layers['thickness'] 
#plt.bar(x,y, color='orange')
#plt.ylabel('Thickness (km)')
#plt.title('Layers of the Earth')
#plt.xlabel('Layersss')
#plt.show()
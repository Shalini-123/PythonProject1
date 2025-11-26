import pandas as pd; 

import matplotlib.pyplot as plt;

print("----------top-song-durations------------")
top=pd.read_csv("c:\\Users\\Shalini\\Documents\\PY_VSCode\\test\\top-song-durations.csv")
print(top.query('duration == duration.min()'))
plt.plot(top['year'],top['duration'])
print(top.info())#
print(top)
top_duration=top['duration'].str.split(':',expand=True)
print(top_duration)
top[['h','m','s']]=top_duration.astype('int')
print(top)
top['total_sec']=top.eval('h*3600 + m*60 + s')
print(top)
plt.bar(top['year'],top['total_sec'])
plt.xlabel('Year')
plt.ylabel('Duration (seconds)')
plt.show()

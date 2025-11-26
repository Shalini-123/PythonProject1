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

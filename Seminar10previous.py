import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#sns.reset_orig()

df = pd.read_csv('california_housing_train.csv')

#fig, ax = plt.subplots()


#plt.scatter(df['longitude'], df['latitude'])



#ax.plot(df['longitude'], df['latitude'])


#plt.scatter(x=df['households'], y=df['population'])

# Load Dataset

#Визуализация нескольких зависимостей

# Plot
# plt.figure(figsize=(10, 8), dpi=80)
# sns.pairplot(df, plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))

# cols = ['population', 'median_income', 'housing_median_age', 'median_house_value']
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)

#Линейные графики

#sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)

#Точечный график с оттенком
#sns.scatterplot(data=df, x="latitude", y="longitude", hue="median_house_value")

#Гистрограммы

#sns.histplot(data=df, x="median_income")

#sns.histplot(data=df, x='housing_median_age')

#sns.histplot(data=df[df['housing_median_age'] > 50], x="median_income")

#Сравнение средних величин по группам

#разделяем на группы
#df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
#df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
#df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'

#выводим
#df.groupby('age_group')['median_income'].mean().plot(kind='bar')

df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'

sns.displot(df, x="median_house_value", hue="income_group")


plt.show()

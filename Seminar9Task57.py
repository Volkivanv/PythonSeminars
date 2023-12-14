from pandas import read_csv
data = read_csv('california_housing_train.csv')
# # 1. Проверить есть ли в файле пустые значения
# print(data.isnull().sum())
# 2. Показать median_house_value где median_income < 2
# res = data[data['medianIncome'] < 2]['medianHouseValue']
# # res = data[data['medianIncome'] < 2]
# print(res)
# 3. Показать данные в первых 2 столбцах
# res = data[['longitude', 'latitude']]
# print(res)
# res = data.iloc[:, :2]          #получение 2-х стлбцов через срезы, 1: - все строки; 2: - только первые 2 слобца
# print(res)
# 4. Выбрать данные где housing_median_age < 20 и  median_house_value > 70000

# res = data[(data['housingMedianAge'] < 20) & (data['medianHouseValue'] > 70_000)]
# print(res)
#print(f"{data['medianIncome']==3.1250]data['medianHouseValue'].max()}")

# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_valu
# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value
# '''
#
# from pandas import read_csv
# data = read_csv('california_housing_test.csv')

# # 1. Определить какое максимальное и минимальное значение median_house_value
# print(f"{data['medianHouseValue'].max()}, {data['medianHouseValue'].min()}")
#
# # # 2. Показать максимальное median_house_value, где median_income = 3.1250
# # print(data[data['median_income'] == 3.1250]['median_house_value'].max())
#
# # # 3. Узнать какая максимальная population в зоне минимального значения median_house_value
# res = data[data['medianHouseValue'] == data['medianHouseValue'].min()]['population'].max()
# print(res)



# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value
# '''
#

# 1. Определить какое максимальное и минимальное значение median_house_value
#print(f"{data['median_house_value'].max()}, {data['median_house_value'].min()}")

# avg = data[(0 <= data['population']) & (data['population'] <= 500)]['median_house_value'].mean()
# print(avg)
#
# 2. Показать максимальное median_house_value, где median_income = 3.1250
# print(data[data['median_income'] == 3.1250]['median_house_value'].max())

# # # 3. Узнать какая максимальная population в зоне минимального значения median_house_value
# res = data[data['median_house_value'] == data['median_house_value'].min()]['population'].max()
# print(res)

# max_households_in_min_population = data[data['population'] == data['population'].min()]['households'].max()
# print(max_households_in_min_population)


# или (если необходимо вывести 2 и более столбцов
# res = data[data['housing_median_age'] < 20][['total_bedrooms', 'total_rooms']]
# print(res)

res = data[['population', 'total_rooms']].median()
print(res)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 1
boston_dataset = load_boston()

print(boston_dataset.keys())

data_frame = pd.DataFrame(data=np.c_[boston_dataset['data']],
                          columns=boston_dataset['feature_names'])
data_frame['MEDV'] = boston_dataset['target']
print(data_frame.head(10))
print(data_frame.tail(10))

# 2
# print(data_frame.info)
print(data_frame.info(verbose=True))
# a 506 obserwacji
# b float 64
# c tak ...

# 3
print(data_frame.describe())
# a wspolczynnik przestepczosci:3.613524 ,odchylenie: 8.601545
# b max: 50.000000, min: 5.000000
# c mediana: 11.360000

# 4
# sns.distplot(data_frame['MEDV'].tolist())
# plt.grid()
# plt.show()

# 5
# print(data_frame.corr())
# print(sns.heatmap(data_frame.corr(), annot=True))
# sns.distplot(data_frame.corr())
# plt.grid()
# plt.show()

# a mocno skorelowane do MEDV jest LSTAT oraz RM
# b niepowiązane z MEDV - CHAS DIS
# c tak rad-tax np

# dodatnio
# sns.regplot(data_frame['MEDV'].tolist(), data_frame['RM'].tolist())
# plt.grid()
# plt.show()

# ujemne
# sns.regplot(data_frame['MEDV'].tolist(), data_frame['LSTAT'].tolist())
# plt.grid()
# plt.show()

# obojetne
# sns.regplot(data_frame['MEDV'].tolist(), data_frame['CHAS'].tolist())
# plt.grid()
# plt.show()

# te dodatnie

# 6
x = data_frame[['LSTAT', 'RM']]
y = data_frame[['MEDV']]

print(train_test_split(x, y, test_size=0.2))

# 7
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
reg = LinearRegression().fit(x_train, y_train)

# train
predictions_2 = reg.predict(x_train)
plt.scatter(y_train, predictions_2)
plt.xlabel('y train')
plt.ylabel('predicted y train')
# plt.show()

# test
predictions = reg.predict(x_test)
plt.scatter(y_test, predictions)
plt.xlabel('y test')
plt.ylabel('predicted y')
# plt.show()

# 8
# a
rmse = mean_squared_error(y_train, predictions_2, squared=False)
print(rmse)
mae = mean_squared_error(y_train, predictions_2)
print(mae)

# b
rmse = mean_squared_error(y_test, predictions, squared=False)
print(rmse)
mae = mean_squared_error(y_test, predictions)
print(mae)






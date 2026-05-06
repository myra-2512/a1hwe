import numpy as np  
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

df= pd.read_csv('Bestsellers with categories.csv')
print(df.head())

print(df.isnull().any())

mode_user_rating = df['User Rating'].mode()
print(mode_user_rating)
median_user_rating = df['User Rating'].median()
print(median_user_rating)
mean_user_rating = df['User Rating'].mean()
print(mean_user_rating)

mode_price = df['Price'].mode()
print(mode_price)
median_price = df['Price'].median()
print(median_price)
mean_price = df['Price'].mean()
print(mean_price)
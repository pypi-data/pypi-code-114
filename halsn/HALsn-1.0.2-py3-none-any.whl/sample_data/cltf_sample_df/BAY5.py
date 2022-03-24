import pandas
import pickle

df = pandas.read_csv('BAY_5-09-14-2021_1014-Cycle26.csv')
# print(df)

pickled_df = pickle.dumps(df)
# print(pickled_df)

#print(pickle.loads(pickled_df))
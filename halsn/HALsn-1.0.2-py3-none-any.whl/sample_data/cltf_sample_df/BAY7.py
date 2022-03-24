import pandas
import pickle

df = pandas.read_csv('BAY_7-09-15-2021_1054-Cycle72.csv')
# print(df)

pickled_df = pickle.dumps(df)
# print(pickled_df)

#print(pickle.loads(pickled_df))
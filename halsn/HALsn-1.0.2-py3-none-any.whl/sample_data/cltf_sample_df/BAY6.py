import pandas
import pickle

df = pandas.read_csv('BAY_6-09-14-2021_1317-Cycle54.csv')
# print(df)

pickled_df = pickle.dumps(df)
# print(pickled_df)

#print(pickle.loads(pickled_df))
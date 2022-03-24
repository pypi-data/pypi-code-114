import pandas
import pickle

df = pandas.read_csv('BAY_4-09-13-2021_1100-Cycle1.csv')
print(df)

pickled_df = pickle.dumps(df)
print(pickled_df)

#print(pickle.loads(pickled_df))
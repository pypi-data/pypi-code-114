#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 23:42:27 2022

@author: patrick
"""


import numpy as np
import pandas as pd
import os, zipfile
from datetime import datetime, timedelta
from tqdm import tqdm



### ENSURES WE SAVE THE ZIPS AS FEATHERS - TO SAVE SPACE ####
def save_in_feather(file_name, delete_csv=False):
    #Read in data - and create time stamp
    print('Reading in:' ,file_name[:-4]+'.csv')
    data=pd.read_csv(file_name[:-4]+'.csv')
    data.columns=[ 'tradeId' 	,'price' 	,'qty' 	,'quoteQty' 	,'time' 	,'isBuyerMaker' 	,'isBestMatch']
    data['date_time']=pd.to_datetime(data['time'],unit='ms' ) 
    if delete_csv: 
        print("Dleting CSV:", file_name[:-4]+'.csv')
        os.remove(file_name[:-4]+'.csv') # delete csv
    #Save as a feather file
    data.to_feather(file_name[:-4])
    print("Saved: ", file_name[:-4])

def create_timings(start_time, end_time, interval=5):
    delta = timedelta(minutes=interval)
    times=[]
    while start_time < end_time:
        times.append(start_time)
        start_time += delta
    times.append(end_time)
    return times
#Creates all timings for the given data frame - and time_interval - in minutes
def all_timings(df, interval):
    start_time=df['date_time'].min().replace(second=0, microsecond=0, nanosecond=0 )
    end_time= df['date_time'].max().replace(hour=23, minute=59, second=59, microsecond=59, nanosecond=59 )
    times = create_timings(start_time, end_time, interval=interval)  #Interval in minutes
    return times


#Calculates the volume weighted price    
def calculate_vwap(relevant_ticks):
    price_volume=0 ; volume=0
    for index, tick in relevant_ticks.iterrows():
        #If tick is a BUY
        price_volume+=(tick[2]*tick[1])  #Volume * Price 
        volume+=tick[2]  #Volue
        return price_volume/volume



def create_candles(df, times):
    candels=[]
    for period in tqdm(range(len(times)-1)):
        #relevant_ticks=sample_ticks[sample_ticks['date_time']]
        relevant_ticks=df[(df['date_time']>= times[period]) & (df['date_time']< times[period+1])]
        if  len(relevant_ticks)>0:
            #Calculate the volume weighted price
            vwap = calculate_vwap(relevant_ticks)
            #Output list
            #['Start_time' , 'End_Time', 'VWAP', 'High', 'Low', 'Open', 'Close']
            candels.append([times[period],times[period+1],vwap, relevant_ticks['price'].max(),relevant_ticks['price'].min(), relevant_ticks['price'].iloc[0], relevant_ticks['price'].iloc[-1]  ])
        else:
            candels.append([times[period],times[period+1],0, 0,0, 0, 0  ])
    return candels
        #tick=relevant_ticks.iloc[0]




############### END IMPORTANT STUFF ################3




coin='BTCUSDT'
base_folder='/home/patrick/Desktop/Crypto_Trading/DATA/TEST/Tick_Data/'


def unpack_zips(base_folder, coin):
    #Finds the files files we care about within the base_folder subdirectories and move the ZIP file contents to base_folder and create Feather Files for them. 
    for subdir, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith('.zip') and coin in file:
                print (os.path.join(subdir, file))
                zip_ref = zipfile.ZipFile(os.path.join(subdir, file)) # create zipfile object        
                zip_ref.extractall(base_folder) # extract file to dir
                zip_ref.close() # close file
                save_in_feather(os.path.join(base_folder, file), delete_csv=True) #Save files as feather to be used later
                print (os.path.join(base_folder, file))



coin='BTCUSDT'
base_folder='/home/patrick/Desktop/Crypto_Trading/DATA/TEST/Tick_Data/'


#Combine all Same currencies in the base directory - into a single file
def create_all_candles(base_folder, coin, candle_size):
    all_candels=[]
    for file in os.listdir(base_folder):
        if coin in file and "Candles" not in file:
            print(file)
            ticks=pd.read_feather(base_folder+file)
            times = all_timings(ticks, candle_size)
            canedls= create_candles(ticks, times)
            all_candels.append(canedls)
            canedls=pd.DataFrame(canedls)
            canedls.to_csv(base_folder+file+'_Candles_%s_Back_up.csv' %candle_size, index=False)
            os.remove(base_folder+file)
    #Combine all files into single file
    flat_list = [item for sublist in all_candels for item in sublist]
    all_candels_df=pd.DataFrame(flat_list )
    all_candels_df.columns=['Opened', 'Closed', 'vwap','High', 'Low', 'Open', 'Close']
    all_candels_df.to_csv(base_folder+'%s_Candles_%s.csv' %(coin,candle_size), index=False)
    
    #Remove temp_files
    for file in os.listdir(base_folder):
        if coin in file and "Back_up" in file:
            os.remove(base_folder+file)
            

        
    
create_all_candles(base_folder, coin, candle_size=25)

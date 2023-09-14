import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#dataset=pd.read_csv(r"C:\Users\Rajesh\Downloads\PAASBAAN-crime-prediction-master\PAASBAAN-crime-prediction-master\data.csv")


data=pd.read_csv(r"C:\Users\nagal\OneDrive\Desktop\desktop files\AI&ML\data.csv")
data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')
    
data['timestamp'] = pd.to_datetime(data['timestamp'], format = '%d-%m/%Y %H:%M:%S')
column_new = data.iloc[:,0]

db=pd.DataFrame({"year": column_new.dt.year,
              "month": column_new.dt.month,
              "day": column_new.dt.day,
              "hour": column_new.dt.hour,
              "dayofyear": column_new.dt.dayofyear,
             # "week": column_new.dt.week,
             # "weekofyear": column_new.dt.weekofyear,
              "dayofweek": column_new.dt.dayofweek,
              "weekday": column_new.dt.weekday,
              "quarter": column_new.dt.quarter,
             })

newdataset=data.drop('timestamp',axis=1)
data1=pd.concat([db,newdataset],axis=1)
data1=data1.dropna()

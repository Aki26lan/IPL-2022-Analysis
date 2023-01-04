import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv(r"C:\Users\UMAPRIYA\Desktop\IPL-2022\IPL 2022.csv")
print(df.head())
profile = ProfileReport(df,title='IPL 2022.csv')
profile.to_file('IPL 2022.csv.html')


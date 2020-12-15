import pandas as pd 
from pandas_profiling import ProfileReport

data = pd.read_csv('Assignment2.csv')
profile = ProfileReport(data)
profile.to_file('report.html')
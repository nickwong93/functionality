import requests
import pandas as pd

data = pd.read_excel ('C:/Users/user/Desktop/Python files/Functional_programs/Sample_dataset/Mini_Sunset_Data.xlsx')

df = pd.DataFrame(data, columns = ['Live links'])

df_list = df['Live links'].values.tolist()

concern_urls = []

for d in df_list:
	r = requests.get(d)
	if r.url != d:
		continue
	else:
		concern_urls.append(d)
output = pd.DataFrame(concern_urls)
output.to_excel(r'C:/Users/user/Desktop/Python files/Functional_programs/Sample_dataset/Mini_Sunset_Data_Output.xlsx', index = False)

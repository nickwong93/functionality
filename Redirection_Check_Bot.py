import requests
import pandas as pd

data = pd.read_excel ('D:/01 NMQ/01 Tasks Documents/2019/01 RMS/149768/EOL list.xlsx')
df = pd.DataFrame(data, columns = ['Permalink Live'])
df_list = df['Permalink Live'].values.tolist()
redirected_urls = []s
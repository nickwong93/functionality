import requests
import pandas as pd

data = pd.read_excel ('D:/01 NMQ/01 Tasks Documents/2019/01 RMS/149768/EOL list.xlsx')
df = pd.DataFrame(data, columns = ['Permalink Live'])
df_list = df['Permalink Live'].values.tolist()
redirected_urls = []

for d in df_list:
	r = requests.get(d)
	redirected_urls.append(r.url)

output = pd.DataFrame(redirected_urls)
output.to_excel(r'D:\01 NMQ\01 Tasks Documents\2019\01 RMS\149768\redirected_links.xlsx', index = False)

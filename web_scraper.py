import requests
import bs4
import pandas as pd

website_url = ""
results = requests.get(website_url)
soup = bs4.BeautifulSoup(result.text,'lxml')
cases = soup.find_all('div' ,class_= 'maincounter-number')

data = []
 
# Find the span and get data from it
for i in cases:
    span = i.find('span')
    data.append(span.string)
 
# Display number of cases
print(data)

df = pd.DataFrame({"CoronaData": data})
 
# Naming the columns
df.index = ['TotalCases', ' Deaths', 'Recovered']

# Exporting data into Excel
df.to_csv('Corona_Data.csv')

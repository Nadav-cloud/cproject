import requests
# continent = 'Asia'
# response = requests.get(f'https://corona.lmao.ninja/v2/continents/{continent}?yesterday&strict')
# print(response.json())
# countries = 'Israel,Italy'
# response = requests.get(f'https://corona.lmao.ninja/v2/countries/{countries}?yesterday')
# res = response.json()
# for c in res:
#     if (c['country'] == 'Israel'):
#         print (c['cases'])

lastDays = 2
# response = requests.get(f'https://corona.lmao.ninja/v2/historical?lastdays={lastDays}')
# print(response.json())
# state='new york'
# response = requests.get(f'https://corona.lmao.ninja/v2/historical/usacounties/{state}?lastdays={lastDays}')
# print(response.json())
response = requests.get(f'https://covid19.richdataservices.com/rds/api/query/int/jhu_country/select?cols=date_stamp,cnt_death,cnt_recovered&where=(iso3166_1=US)&format=amcharts&limit=5000')
print(response.json())



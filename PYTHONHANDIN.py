
'''
#Python hand-in
#Part1
import json
from collections import Counter
#Seattle,WA,GHCND:US1WAKG0038
seattle_prec = []
monthly_precip = []
with open('precipitation.json') as file:
    precipitations = json.load(file)
sum_month_precip = Counter()        
for measurement in precipitations:
    if measurement['station'] == 'GHCND:US1WAKG0038': #This only gives me the dictionaries with that code
        split_date_month = measurement['date'].split("-")[1]
        measurement['date'] = split_date_month #split_date_month only month  
        sum_month_precip[measurement['date']] += measurement['value']
#print(sum_month_precip)
with open('precipitationSE.json', 'w') as file:
    json.dump(precipitations, file, indent=4)
'''
#Part3
#Calculate the sum of the parts over the whole year: only seattle or all of them?
#This is only a sum per month
import json
from collections import Counter

with open('precipitation.json') as file:
    precipitations = json.load(file)

sum_year_precip = Counter()

for measurement in precipitations:
    split_date_year = measurement['date'].split("-")[0]
    print(split_date_year)
    measurement['date'] = split_date_year #split_date_month only month  
    sum_year_precip[measurement['date']] += measurement['value']
    sum_year_precip[measurement['date']] += measurement['value']

print(sum_year_precip)


#Calculate the relative precipation per month(percentage compared to the precipitation over the whole year)

# sum_year_precip = {'2010' : 151023}
# total precipitation for all cities
# total precipitation per month for Seattle
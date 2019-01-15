#Part2
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

print(sum_month_precip)

total_year_seattle = 0
for month_rain in sum_month_precip:
    print(sum_month_precip[month_rain])
    total_year_seattle += sum_month_precip[month_rain]

print(f'The total yearly rainfall for Seattle is {total_year_seattle}')


with open('precipitationSE.json', 'w') as file:
    json.dump(precipitations, file, indent=4)

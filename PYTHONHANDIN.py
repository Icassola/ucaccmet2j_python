'''
[1, 2, 5, 6, 7, 7, 5, 4]

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
sum_january_precip = Counter()        
for measurement in precipitations:
    if measurement['station'] == 'GHCND:US1WAKG0038': #This only gives me the dictionaries with that code
        split_date_month = measurement['date'].split("-")[1]
        measurement['date'] = split_date_month #split_date_month only month  
        sum_january_precip[measurement['date']] += measurement['value']
print(sum_january_precip)
with open('precipitationSE.json', 'w') as file:
    json.dump(students, file, indent=4)
from django.db import models

# Create your models here.

import coinmarketcap
import json
#import pandas as pd
import time

market = coinmarketcap.Market()
json_result = market.ticker('', limit=10, convert='USD')

result = []
result_line = []
for j in json_result:
    result_line = []
    result_line.append(j['name'])
    result_line.append(j['price_usd'])
    result_line.append(j['percent_change_24h'])
    result_line.append(j['percent_change_7d'])
    result.append(result_line)

#print(result)

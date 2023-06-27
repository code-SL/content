import pandas as pd
import numpy as np
import json
from icecream import ic
from pandas_market_calendars import get_calendar

import random
import datetime

def generate_trading_dates(start_date, end_date):
    calendar = get_calendar('NYSE')
    trading_dates = calendar.schedule(start_date=start_date, end_date=end_date)
    trading_dates = trading_dates.index.date.tolist()

    return trading_dates

start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-06-01')


trading_dates = generate_trading_dates(start_date, end_date)

string_list = [dt.strftime("%Y-%m-%d") for dt in trading_dates] 
ic(string_list)
ic(len(string_list))


minimum_value = 1
num_steps = len(string_list)

def gen_prices(start_low,start_high):
    starting_point = random.randrange(start_low,start_high)
    increments = np.random.normal(0, 1, num_steps)
    random_walk = np.cumsum(increments) + starting_point
    random_walk = np.maximum(random_walk, minimum_value)
    return random_walk

data = []
num_runs = 3
column_tickers = ['tickerA','tickerB','tickerC']

for run in range(num_runs):
    prices = gen_prices(1,100)
    data.append(prices)

df = pd.DataFrame(data).transpose()
df.index = string_list
df.columns = column_tickers
ic(df)

example_json = df.reset_index(names=['date']).to_dict(orient="records")
ic(example_json)

with open('example.json', 'w') as f:
    json.dump(example_json, f)
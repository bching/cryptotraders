from flask import render_template
from cryptotraders import app 

import json, operator, re

import requests
import ast

class Strategy:
    def __init__(self, strategy, value):
        self.strategy = strategy
        self.value = value

def get_raw_info():
    url = "http://ec2-18-236-98-219.us-west-2.compute.amazonaws.com/bitcoin_arbitrager"
    raw_data = requests.get(url).json()
    strategies = sorted(raw_data['strategies'].items(), key=operator.itemgetter(1), reverse=True)
    prices = raw_data['prices']

    data = []
    p = re.compile("'([^']*)'")

    for row in strategies:
        strats = []
        m = re.findall(p, row[0])

        start,market,end = ('','','')

        for i in range(0, len(m)):
            start,market,end = m[i].split(">")
            ask,bid= 0,0
            
            for price in prices:
                if price['name'] == market: 
                    if price['key0'] == start and price['key1'] == end or price['key0'] == end and price['key1'] == start:
                        ask = price['ask']
                        bid = price['bid']
                    
            strat_obj = {'name':market, 'key0':start , 'key1':end, 'ask':ask, 'bid':bid}
            print(strat_obj)

            strats.append(strat_obj)

        if len(strats) < 3:
            for i in range(len(strats) - 1, 2):
                strats.append('')

        value = row[1] 
        data.append(Strategy(strats, value))
       
    return data 

@app.route('/')
def index():
    strategies = get_raw_info()

    return render_template('base.html', strategies=strategies)

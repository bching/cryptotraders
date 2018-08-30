from flask import render_template
from cryptotraders import app 

import requests, json, operator, re

class Strategy:
    def __init__(self, strategy, value):
        self.strategy = strategy
        self.value = value

def get_raw_info():
    url = "http://ec2-18-236-98-219.us-west-2.compute.amazonaws.com/bitcoin_arbitrager"
    raw_data = requests.get(url).json()
    strategies = sorted(raw_data['strategies'].items(), key=operator.itemgetter(1), reverse=True)

    data = []
    p = re.compile("'([^']*)'")

    for row in strategies:
        strats = []
        m = re.findall(p, row[0])
        size = 3 - len(m)
        for i in range(0, len(m)):
            strats.append(m[i])
        if len(m) < 3:
            for i in range(len(m) - 1, 2):
                strats.append('')

        value = row[1] 
        data.append(Strategy(strats, value))
       
    return data 

@app.route('/')
def index():
    strategies = get_raw_info()

    return render_template('base.html', strategies=strategies)

import requests
import ast
import operator, re
import json

#def get_raw_info():
#    raw_data = _get_raw_info_origin()
#    raw_data['strategies'] = {
#        ast.literal_eval(raw_str_key + ' a'): value
#        for raw_str_key, value in list(raw_data['strategies'].items())
#    }
#    return raw_data


def get_parsed_info():
    raw_data = get_raw_info()
    new_prices = []
    #for route_dict in raw_data['prices']:
        #route_dict['bidkey'] = '>'.join(
        #    [route_dict['key0'], route_dict['name'], route_dict['key1']])
        #route_dict['askkey'] = '>'.join(
        #    [route_dict['key1'], route_dict['name'], route_dict['key0']])
    #    new_prices.append(route_dict)

    return raw_data
    # for strategy in strategies:
    #     new_strategy_dict=
    #     routes_tuple,value=strategy
    #     for route in routes_tuple:
    #         from_,exchange,to_=route.split('>')
    #         {'from':from_,'to':to_}

    #return raw_data

class Strategy:
    def __init__(self, strategy, value, ask_price = 0, bid_price = 0):
        self.strategy = strategy
        self.value = value

def get_raw_info():
    url = "removed for security"
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
                    
            #print(start,market,end,ask,bid)
            strat_obj = {'name':market, 'key0':start , 'key1':end, 'ask':ask, 'bid':bid}

            #strats.append(m[i])
            strats.append(strat_obj)

        #strats.append(exch)
        #print(strats)
        #if len(m) < 3:
        #    for i in range(len(m) - 1, 2):
        #        strats.append('')

        value = row[1] 
        data.append(Strategy(strats, value))
       
    return data 

if __name__ == '__main__':
    from pprint import pprint
    print(get_raw_info())
    #pprint(get_parsed_info())

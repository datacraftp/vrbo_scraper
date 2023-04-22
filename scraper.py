import requests
import json
from payload import payload_data
import csv

URL = 'https://www.vrbo.com/graphql'

headers = {
    
    'client-info':'shopping-pwa,unknown,unknown',
    'content-type':'application/json',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

    }
list_data = []
def get_api_data(page:int,checkin:str,checkout:str, region:str):
    checkin = checkin.split('/')    
    checkout = checkout.split('/')
    

    print(f'Page Number Scraping..{page}')
    
    data = json.loads(payload_data)
    #Set payload payload
    data[0]['variables']['criteria']['secondary']['counts'][0]['value'] = page
    #Set the Checkin payload
    #Day
    data[0]['variables']['criteria']['primary']['dateRange']['checkInDate']['day'] = int(checkin[0])
    #Month
    data[0]['variables']['criteria']['primary']['dateRange']['checkInDate']['month'] = int(checkin[1])
    #year
    data[0]['variables']['criteria']['primary']['dateRange']['checkInDate']['year'] = int(checkin[2])

    #Set the Checkout Payload
    #Day
    data[0]['variables']['criteria']['primary']['dateRange']['checkOutDate']['day'] = int(checkout[0])
    #Month
    data[0]['variables']['criteria']['primary']['dateRange']['checkOutDate']['month'] = int(checkout[1])
    #year
    data[0]['variables']['criteria']['primary']['dateRange']['checkOutDate']['year'] = int(checkout[2])
    #Set the region in payload
    data[0]['variables']['criteria']['primary']['destination']['regionName'] = str(region)

    # print(data)
    req = requests.post(URL, headers=headers,json=data)    
    req_json = req.json()[0]
    
    
    return req_json

# print(data)
def data_filter(data):
    local_dlist  = []

    listing= data['data']['propertySearch']['propertySearchListings']

    for x in listing:
        
        try:
            
            url = x['cardLink']['resource']['value'].split('?')[0]
            title = x['headingSection']['heading']
            price = x['priceSection']['priceSummary']['displayMessages'][0]['lineItems'][0]['price']['formatted']
            try:
                rating = x['summarySections'][0]['guestRating']['parts'][0]['text']

            except IndexError:
                rating = 'No Rating'
            
            make_d = {
                        'url': url,
                        'title': title,    
                        'rating':rating,                    
                        'price':price
                    }
            
            local_dlist.append(make_d)

        except (KeyError):            
            pass

    if len(local_dlist)>=1:
        return local_dlist
    else:
        return None


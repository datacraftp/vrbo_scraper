import requests
import json
from payload import payload_data, payload_comments
from tools import extract_busines_id

URL = 'https://www.vrbo.com/graphql'

headers = {
    
    'client-info':'shopping-pwa,unknown,unknown',
    'content-type':'application/json',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

    }

def get_api_data(page:int,checkin:str,checkout:str, region:str):
    checkin = checkin.split('/')    
    checkout = checkout.split('/')
    

    print(f'Page Number Scraping..{page}')
    
    data = json.loads(payload_data)
    #Set payload page
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
    
    req = requests.post(URL, headers=headers,json=data)    
    req_json = req.json()[0]    
    
    return req_json


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

def scrape_coments(url):
   
    busines_id = extract_busines_id(url)
    payload_json_c = json.loads(payload_comments)
    #Add busines id to the payload
    payload_json_c[0]['variables']['propertyId'] = busines_id   

    req = requests.post(URL, headers=headers,json=payload_json_c)
    reviews_json_data = req.json()[0]['data']['propertyInfo']['reviewInfo']['reviews']
    coment_list = []

    for x in reviews_json_data:
        coment_data = {
                        'url': url.strip(),
                        'busines_id': busines_id,
                        'title': x['title'].strip(),
                        'text' : x['text'].strip(),
                        'author': x['reviewAuthorAttribution']['text'].strip(),
                        'comment_date': x['submissionTime']['longDateFormat'].strip(),
                        'rating': x['reviewScoreWithDescription']['value'].strip()                     
                    }
        coment_list.append(coment_data)
    return coment_list

def scrape_hotels(check_in_date,check_out_date,region):

    page = 0  
    list_data = []
    while True:
        
        data = get_api_data(page,check_in_date,check_out_date,region) 
        results = data_filter(data)
        if results != None:
            list_data.extend(results)            
            page += 50
        else:
            print('Scraped Finised')
            break
    return list_data


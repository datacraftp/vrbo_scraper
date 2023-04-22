from scraper import *

#Format Day/Month/Year
check_in_date = '13/11/2023'
check_out_date = '14/11/2023'
region  = 'New york, New york, United States of America'

if __name__ == '__main__':
    page = 0  

    while True:
        
        data = get_api_data(page,check_in_date,check_in_date,region) 
        results = data_filter(data)
        if results != None:
            list_data.extend(results)            
            page += 50
        else:
            print('Scraped Finised')
            break

    with open('data.csv', 'w',newline='',encoding='utf-8')as csvfile:
        headers = ['url','title','rating','price']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for data in list_data:           
            writer.writerow(data)

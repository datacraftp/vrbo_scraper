from scraper import *
from tools import save_to_database_hotels,get_url_from_db,save_to_databse_comments
import argparse
import json

parser = argparse.ArgumentParser(description='Scrape hotels and/or comments.')
parser.add_argument('--config', type=str, help='Configuration file in JSON format.')

args = parser.parse_args()

if args.config:
    with open(args.config) as f:
        config = json.load(f)        

    if config.get('hotels'):
        check_in_date = config.get('check_in')
        check_out_date = config.get('check_out')
        region = config.get('region')
        list_data = scrape_hotels(check_in_date,check_out_date,region)
        save_to_database_hotels('hotels_data', list_data)

    if config.get('comments'):

        #Scrape comments from the urls added to DB
        urls_list = get_url_from_db('hotels_data.db')

        ##Scraping comments..
        if urls_list != None:
            list_coments = []
            for url in urls_list:
                results = scrape_coments(url[0])
                list_coments.extend(results)

            print("Done Scraping Comments!")

            #Write Comments to DB
            save_to_databse_comments('comments_data.db', list_coments)
    else:
        print('No option has been selected, please update config.json file!')    

else:
    print('Error: Configuration file not provided')
    parser.print_help()



import re
import csv
import sqlite3

def extract_busines_id(url_data):
    
    pattern = r'h(\d+)'
    extract = re.search(pattern, url_data)
    if extract:
        b_id = extract.group(1)
        print(b_id )
        return b_id
    else:
        return None
    
def write_csv(data_to_write):

    with open('data.csv', 'w',newline='',encoding='utf-8')as csvfile:
        headers = ['url','title','rating','price']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for data in data_to_write:           
            writer.writerow(data)

def save_to_databse_comments(name:str,data:list):
    
    connection = sqlite3.connect(name)
    c = connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS coments(url,business_id, title, text, author, coment_date, rating)')
    
    for coment in data:
        c.execute('INSERT INTO coments VALUES (:url,:business_id, :title, :text, :author, :comment_date, :rating)', {'url':coment['url'],'business_id':coment['busines_id'],'title':coment['title'],'text':coment['text'],'author':coment['author'],'comment_date':coment['comment_date'],'rating':coment['rating']})
    connection.commit()
    connection.close()

def save_to_database_hotels(name:str,data:list):

    name = name + '.db'
    connection = sqlite3.connect(name)
    c = connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS hotels(url,title,rating,price)')

    for hotel in data:
        c.execute('INSERT INTO hotels VALUES(:url,:title,:rating,:price)',{'url':hotel['url'], 'title':hotel['title'],'rating':hotel['rating'],'price':hotel['price']})
    connection.commit()
    connection.close()

def get_url_from_db(name_db:str):
    try:
        with sqlite3.connect(name_db) as conn:
            c = conn.cursor()
            c.execute(f'SELECT url FROM hotels')
            url_list = c.fetchall()
            return url_list
    except sqlite3.OperationalError:
        print('There are no urls in the DB, you need to scrape them first!')

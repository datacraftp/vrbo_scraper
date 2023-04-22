# VRBO SCRAPER
This project is a web scraper written in Python that extracts information from a vacation rental website using GraphQL API.

## Getting Started
To use this program, you will need to have Python 3.x installed on your machine.

## Prerequisites
- Python 3.x
- requests module
- json module
- csv module

## Usage
- Open the main.py file in a text editor.
- Set the check_in_date, check_out_date, and region variables to your desired values.
- Run the main.py file to start the web scraping process.
- The scraped data will be saved to a data.csv file in the same directory.
### Code Overview
- The project consists of two files: scraper.py and main.py.

- scraper.py
This file contains the functions responsible for extracting data from the website.

- main.py
- This file imports the get_api_data() and data_filter() functions from scraper.py and uses them to scrape data from the website. The scraped data is saved to a CSV file.


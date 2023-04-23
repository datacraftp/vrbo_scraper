# VRBO SCRAPER
This project is a web scraper written in Python that extracts information from a vacation rental website using GraphQL API.

## Getting Started
To use this program, you will need to have Python 3.x installed on your machine.

## Prerequisites
- Python 3.x
- requests module
- json module
- csv module
## JSON configuration file

The JSON configuration file should contain the following fields:
```JSON
{
    "hotels": true,
    "check_in": "13/09/2023",
    "check_out": "14/09/2023",
    "region": "New york, New york, United States of America",
    "comments": true
}
```
If you set 'hotels': false, it will only scrape the comments for the urls that are already in the DB.
If you set 'comments': false, it will only scrape hotels.
Set true if you want both option to be done.
## Usage
- Set the config.json file with desired option
- To run the script, execute the following command:
```python main.py --config config.json```
- The scraped data will be saved to sqlite3 database file in the same directory.


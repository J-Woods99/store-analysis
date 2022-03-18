
###########################
#                         #
#    SHOP FOOD SCALPER    #
#      BY MR. WOODS       #
###########################

# NOTES
# https://www.iceland.co.uk/sitemap

# MODULES
import json
import requests
from bs4 import BeautifulSoup

# CONSTANTS

# VARIABLES

# SCALPER INIT
url = 'https://www.iceland.co.uk/p/iceland-chicken-tenders-350g/88603.html'  # Tendie tester
result = requests.get(url)
doc_html = BeautifulSoup(result.text, 'html.parser')
doc_json = BeautifulSoup(result.content, 'html.parser')

# This handles the name and
json_script = doc_json.find_all('script')[3].text.strip()
json_data = json.loads(json_script)
item_name = json_data['name']  # Name of item
item_price = json_data['offers']['price']  # Price of item


# print(doc_html)
# print(doc.prettify())

# prices = doc_html.find_all(text='price')
# print(prices)


# SCALPER FUNCTION


# -- Error checking
# print(doc_json.title)
print(json_data)
print(item_name)
print(item_price)

# EXCEL INIT


# SEND TO EXCEL

# MAIN

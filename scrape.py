
from bs4 import BeautifulSoup
import requests

#page_link  = 'https://www.zillow.com/manhattan-new-york-ny-10007/?searchQueryState={%22pagination%22:{},%22usersSearchTerm%22:%2210007%22,%22mapBounds%22:{%22west%22:-74.01448844714355,%22east%22:-74.00024055285644,%22south%22:40.710634221558685,%22north%22:40.716166870622764},%22regionSelection%22:[{%22regionId%22:61621,%22regionType%22:7}],%22isMapVisible%22:true,%22mapZoom%22:17,%22filterState%22:{%22isAllHomes%22:{%22value%22:true}},%22isListVisible%22:true}'
page_link ='https://www.century21.com/real-estate/new-york-ny-10007/LZ10007/?ty=0'
page_response = requests.get(page_link, timeout=5)

soup = BeautifulSoup(page_response.content, "html.parser")

#print(str(soup))

address_list = []
price_list = []

#for zillow. They have a captcha in place to prevent scraping.
#this_address = page_content.find_all("div", {"class": "list-card-addr"})[0].text
#this_price = page_content.find_all("div", {"class": "list-card-price"})[0].text

#this_address = page_content.find_all("div", attrs={"class": "property-card"}) 
#address_list.append(this_address)
#price_list.append(this_price)
#print([item["data-address"] for item in page_content.find_all('div', attrs={'class': 'property-card', "data-address": True})])

#these work but we want a single object
#my_addresses = soup.findAll('div', attrs={'class': 'property-address'})
#my_prices = soup.findAll('a', attrs={'class': 'listing-price'})
#my_beds = soup.findAll('div', attrs={'class': 'property-beds'})

#print(my_addresses[0].text)
#print(my_addresses[1].text)

#print(str(len(my_addresses)) + '; ' + str(len(my_prices)) + '; ' +  str(len(my_beds)))
#for i in range(0, len(my_addresses)):
#	#print(my_addresses[i].text +', ' +  my_prices[i].text + my_beds[i].text)
#	address_list.append(my_addresses[i])

my_results = soup.findAll('div', attrs={'class':'property-card-primary-info'})
#print(str(my_results))
for i in range(0, len(my_results)):
	price = my_results[i].find('a', attrs={'class': 'listing-price'})
	bed = my_results[i].find('div', attrs={'class': 'property-beds'})
	address = my_results[i].find('div', attrs={'class': 'property-address'})
	if price is not None:
		price = price.text.strip()
	else:
		price = ""
	if bed is not None:
		bed = bed.text.strip()
	else: 
		bed = ""
	if address is not None:
		address = address.text.strip()
	else:
		address = ""
	print(str(price) + '; ' +  str(address) + '; ' + str(bed) +  '; ')


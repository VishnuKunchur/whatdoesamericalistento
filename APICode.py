import eventful
from bs4 import BeautifulSoup
import requests
import pandas as pd

url1 = 'http://api.eventful.com/rest/events/search?app_key=F4W73GDqFFxTBTRG&q=music&l=Los+Angeles&date=2017010100-2017123100&page_size=100'
response = requests.get(url1)
data = response.text
dataxml = BeautifulSoup(data, 'lxml')
maxpagenum = int(dataxml.find('page_count').string)

page_num = []
for i in range(1,(maxpagenum+1)):
    page_num.append('http://api.eventful.com/rest/events/search?app_key=F4W73GDqFFxTBTRG&q=music&l=Los+Angeles&t=Today&page_size=100&page_number='+str(i))
    
urltest = 'http://api.eventful.com/rest/events/search?l=Los+Angeles&app_key=F4W73GDqFFxTBTRG&date=2017010100-2017123100&page_size=250'
response = requests.get(urltest)
data = response.text
dataxml = BeautifulSoup(data, 'lxml')

ev_title = []
ev_sttime = []
ev_venuename = []
ev_venueadd = []
ev_cityname = []
ev_pc =[]
ev_lat = []
ev_lon = []
ev_pername = []
ev_perbio = []


for ev in dataxml.find_all('event'):
    if ev.performers.contents != []:
        ev_title.append(ev.title.string)
        ev_sttime.append(ev.start_time.string)
        ev_venuename.append(ev.venue_name.string)
        ev_venueadd.append(ev.venue_address.string)
        ev_cityname.append(ev.city_name.string)
        ev_pc.append(ev.postal_code.string)
        ev_lat.append(ev.latitude.string)
        ev_lon.append(ev.longitude.string)
        ev_pername.append(ev.performers.performer.name)
        ev_perbio.append(ev.performers.performer.short_bio.string)

xmldf = pd.DataFrame(list(zip(ev_title,ev_sttime,ev_venuename,ev_venueadd,ev_cityname,ev_pc,ev_lat,ev_lon,ev_pername,ev_perbio)))
        
        
        


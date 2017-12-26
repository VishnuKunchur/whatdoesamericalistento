def ConcertDF(USstateCode, Genre, StartDate, EndDate, APIKey):
    import ticketpy
    import pandas as pd
    try:
        tm_client = ticketpy.ApiClient(APIKey)
    except: 
        'Enter a valid API key!'
    pages = tm_client.events.find(
            classification_name = Genre,
            state_code = USstateCode,
            start_date_time = StartDate + 'T00:00:00Z', ##StartDate Format: YYYY-MM-DD
            end_date_time = EndDate + 'T00:00:00Z' ##EndDate Format: YYYY-MM-DD
            )
    if pages.page == []:
        concerts = pd.DataFrame(columns = ('Event', 'Genre', 'SubGenre', 'ArtistType', 'ImageURL', 'EventInfo', 'StartTime',
                                      'EndTime', 'VenueAddress', 'PostalCode', 'City', 'State', 'StateCode', 'Address',
                                      'Longitude', 'Latitude', 'MinTicketPrice', 'MaxTicketPrice')) 
        return concerts
    else:
        ev_name = []
        ev_genre = []
        ev_subgenre = []
        ev_artisttype = []
        ev_image = []
        ev_info = []
        ev_sttime = []
        ev_entime = []
        ev_venue = []
        ev_pc = []
        ev_city = []
        ev_state = []
        ev_statecode = []
        ev_address = []
        ev_lon = []
        ev_lat = []
        ev_minpr = []
        ev_maxpr = []
    
        for page in pages:
            for event in page:
                try:
                    ev_name.append(event.json['name'])
                except KeyError:
                    ev_name.append('NA')
                try:                                                                                        
                    ev_genre.append(event.json['classifications'][0]['genre']['name'])
                except KeyError:
                    ev_genre.append('NA')
                try:
                    ev_subgenre.append(event.json['classifications'][0]['subGenre']['name'])
                except KeyError:
                    ev_subgenre.append('NA')
                try:
                    ev_artisttype.append(event.json['classifications'][0]['type']['name']  )                
                except KeyError:                                                                            
                    ev_artisttype.append('NA')                                                                                    
                try:
                    ev_image.append(event.json['images'][0]['url'])
                except KeyError:
                    ev_image.append('NA')
                try:
                    ev_info.append(event.json['pleaseNote'])
                except KeyError:
                    ev_info.append('NA')
                try:
                    ev_sttime.append(event.json['sales']['public']['startDateTime'])
                except KeyError:
                    ev_sttime.append('NA')
                try:
                    ev_entime.append(event.json['sales']['public']['endDateTime'])
                except KeyError:
                    ev_entime.append('NA')
                try:
                    ev_venue.append(event.json['_embedded']['venues'][0]['name'])
                except KeyError:
                    ev_venue.append('NA')
                try:    
                    ev_pc.append(event.json['_embedded']['venues'][0]['postalCode'])
                except KeyError:
                    ev_pc.append('NA')
                try:
                    ev_city.append(event.json['_embedded']['venues'][0]['city']['name'])
                except KeyError:
                    ev_city.append('NA')
                try:
                    ev_state.append(event.json['_embedded']['venues'][0]['state']['name'])
                except KeyError:
                    ev_state.append('NA')
                try:
                    ev_statecode.append(event.json['_embedded']['venues'][0]['state']['stateCode'])
                except KeyError:
                    ev_statecode.append('NA')
                try:
                    ev_address.append(event.json['_embedded']['venues'][0]['address']['line1'])
                except KeyError:
                    ev_address.append('NA')
                try:
                    ev_lon.append(event.json['_embedded']['venues'][0]['location']['longitude'])
                except KeyError:
                    ev_lon.append('NA')
                try:    
                    ev_lat.append(event.json['_embedded']['venues'][0]['location']['latitude'])
                except KeyError:
                    ev_lat.append('NA')
                try:
                    ev_minpr.append(event.json['priceRanges'][0]['min'])
                except KeyError:
                    ev_minpr.append('NA')
                try:
                    ev_maxpr.append(event.json['priceRanges'][0]['max'])
                except KeyError:
                    ev_maxpr.append('NA')
        
        concerts = pd.DataFrame(list(zip(ev_name, 
                                         ev_genre,
                                         ev_subgenre,
                                         ev_artisttype,
                                         ev_image,
                                         ev_info,
                                         ev_sttime,
                                         ev_entime,
                                         ev_venue,
                                         ev_pc,
                                         ev_city,
                                         ev_state,
                                         ev_statecode,
                                         ev_address,
                                         ev_lon,
                                         ev_lat,
                                         ev_minpr,
                                         ev_maxpr)))
        concerts.columns = ['Event', 'Genre', 'SubGenre', 'ArtistType', 'ImageURL', 'EventInfo', 'StartTime',
                            'EndTime', 'VenueAddress', 'PostalCode', 'City', 'State','StateCode','Address',
                            'Longitude', 'Latitude', 'MinTicketPrice', 'MaxTicketPrice']
        return concerts
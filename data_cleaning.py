import pandas as pd

#read file
df = pd.read_csv('D:/Users/rsilva/Documents/Python Scripts/webscrap/projects/tripadvisor/test.csv')
print(df.head())
print(df.shape)

def clean_df(df):
    '''
    remove special characters and unwanted words from scraped data
    '''

    df['mail'] = df['mail'].str.replace('mailto:','').str.replace('\?subject=\?','')
    df['phone_number'] = df['phone_number'].str.replace('tel:','')
    df['ranking_subclass_1'] = df['ranking_subclass_1'].str.replace(u'N.º\xa0',u'')
    df['ranking_subclass_2'] = df['ranking_subclass_2'].str.replace(' de ','')
    df['ranking_city_1'] = df['ranking_city_1'].str.replace(u'N.º\xa0',u'')
    df['ranking_city_2'] = df['ranking_city_2'].str.replace(' de ','')

    return df



###obtain lon and lat from address column
from geopy.geocoders import GoogleV3


def get_coordinates(df):
    '''
    get longitude and latitude from address using geopy and google geolocator
    '''
    geolocator = GoogleV3(api_key='AIzaSyDHRHmKwOECP1sa70CYXvbq_1gBxTtZ5hc') #must insert valid google API

    latitudes=[]
    longitudes=[]
    addresses = df['address'].tolist()
    for address in addresses:
        try:

            location = geolocator.geocode(address)
            if location is not None:
                latitudes.append(location.latitude)
                longitudes.append(location.longitude)
            else:
                print(f"Could not find Location for {address!r}")
                latitudes.append('NA')
                longitudes.append('NA')
        except GeocoderUnavailable as e:
            latitudes.append('NA')
            longitudes.append('NA')

    df = df.assign(lat = latitudes)
    df = df.assign(lon = longitudes)

    return df

#export to csv
df.to_csv('tripadvisor_restaurants.csv', index = False, encoding='utf-8-sig')


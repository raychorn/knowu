import requests
import json

__url__ = 'http://api.sba.gov/geodata/city_county_links_for_state_of/{{state}}.json'

states = [
"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
"HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
"MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
"NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
"SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

def fetch_data(url):
    __data__ = {}
    try:
        r = requests.request('GET', url)
        if (r.status_code == 200):
            __data__ = r.json()
        r.raise_for_status()
    except:
        raise requests.HTTPError
    return __data__

def fetch_data_for(state):
    url = __url__.replace('{{state}}', str(state).lower())
    try:
        __data__ = fetch_data(url)
    except:
        __data__ = None
    return __data__


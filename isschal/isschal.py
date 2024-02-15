#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    # Determine Lat & Lon
    lat = resp['iss_position']['latitude']
    lon = resp['iss_position']['longitude']
    
    return lat, lon

    lat, lon = get_iss_location()

    print(f""" Current Location of the ISS:
    Lon: {lon}
    Lat: {lat}
    """)
if __name__ == "__main__":
    main()


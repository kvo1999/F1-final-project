import requests
import json

#products_url = "https://ergast.com/api/f1/2021/5/driverStandings.json"

products_url = "https://ergast.com/api/f1/2021/5/driver/alonso/laps.json"

products_response = requests.get(products_url)


products = json.loads(products_response.text)
print(products['MRData'])

#driver_data = []
#for k,v in products['MRData']['StandingsTable'].items():
 #   driver_data.append({
         


    #})
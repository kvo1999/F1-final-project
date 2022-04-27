import requests
import json

driver_lname = input("Please enter the driver's last name you wish to analyze: ")

ergast_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/status.json"


ergast_response = requests.get(ergast_url)


ergast = json.loads(ergast_response.text)

print(driver_lname)



n = 0


for line in ergast['MRData']['StatusTable']['Status']:
   finish_status = ergast['MRData']['StatusTable']['Status'][n]['status']
   number_finish_status = ergast['MRData']['StatusTable']['Status'][n]['count']
   print(finish_status, number_finish_status)
   n = n + 1



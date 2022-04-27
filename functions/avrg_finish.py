import requests
import json
import statistics

driver_lname = input("Please enter the driver's last name you wish to analyze: ")

ergast_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/results.json"

ergast_response = requests.get(ergast_url)

ergast = json.loads(ergast_response.text)

print(driver_lname)

n = 0
x = 0

grid = []
finish = []

for line in ergast['MRData']['RaceTable']['Races']:
   finish_result = line['Results'][0]['position']
   starting_grid = line['Results'][0]['grid']
   finish.append(int(finish_result))
   grid.append(int(starting_grid))
   n = n + 1

print(grid)
print(finish)
print("Average starting grid position:", int(statistics.mean(grid)))
print("Average finish position:", int(statistics.mean(finish)))






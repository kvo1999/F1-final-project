import requests
import json
import statistics
import datetime

total_rounds = 22 #global variable to hold the number of rounds in the f1 2021 season

def average_finish(driver_lname):
  """
  Calculates a driver's average starting grid position and average finishing position.

  Parameters:
    driver_lname (str): a string of the driver's last name, like "alonso"
  
  Returns:
    resultfin (dict): a dictionary containing two key-value pairs: {"Average Starting Grid": avg_grid, "Average Finishing Position": avg_finish}
      avg_grid (int): an integer of the driver's average starting grid position
      avg_finish (int): an integer of the driver's average finishing position

  Invoke like this: average_finish("alonso")
  Example return value: {"Average Starting Grid": 3, "Average Finishing Position": 5}
  """

  ergast_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/results.json"
  ergast_response = requests.get(ergast_url)
  ergast = json.loads(ergast_response.text)
    
  n = 0

  grid = []
  finish = []

  for line in ergast['MRData']['RaceTable']['Races']:
    finish_result = line['Results'][0]['position']
    starting_grid = line['Results'][0]['grid']
    finish.append(int(finish_result))
    grid.append(int(starting_grid))
    n = n + 1
  
  avg_grid = round(statistics.mean(grid))
  avg_finish = round(statistics.mean(finish))

  resultfin = {"Average Starting Grid": avg_grid, "Average Finishing Position": avg_finish}

  return resultfin

def reason_DNF(driver_lname):
  """
  Outlines all the reasons a driver did not finish a race and how many times this happened to them.

  Parameters:
    driver_lname (str): a string of the driver's last name, like "alonso"

  Returns:
    resultDNF (dict): a dictionary containing two key-value pairs: {"Finishing Status": status, "Count": count}
      status (list): a list of all the driver's finishing statuses
      count (list): a list corresponding the number of times a driver had a certain finishing status
    
  Invoke like this: reason_DNF("alonso")
  Example return value: {"Finishing Status": ['Finished', 'Collision'], "Count": ['21','1']}
  """
  ergast_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/status.json"
  ergast_response = requests.get(ergast_url)
  ergast = json.loads(ergast_response.text)

  return ergast["MRData"]["StatusTable"]["Status"]

def podium_result(driver_lname):
  """
  Calculates the total number of times a driver came in first, second, and third place each.

  Paramters:
    driver_lname (str): a string of the driver's last name, like "alonso"
  
  Returns:
    resultpodium (dict): a dictionary containing three key-value pairs:
      {"First place: ":podiums.count("1"), "Second place: ":podiums.count("2"), "Third place: ":podiums.count("3")}
        podiums.count("1") (int): an integer corresponding the the total number of times a driver got first place
        podiums.count("2") (int): an integer corresponding to the total number of times a driver got second place
        podiums.count("3") (int): an integer corresponding to the total number of times a driver got third place

  Invoke like this: podium_result("alonso")
  Example return value: {"First place: 8, "Second place: ": 0, "Third place: ": 1}
  """

  circuit=["yas_marina","jeddah","bahrain","catalunya","istanbul","americas","sochi","monza","zandvoort","spa","hungaroring","silverstone","ricard","BAK","rodriguez","interlagos","losail","monaco","portimao","imola", "red_bull_ring"]
  circuitraikkonen= ["yas_marina","jeddah","bahrain","catalunya","istanbul","americas","sochi","spa","hungaroring","silverstone","ricard","BAK","rodriguez","interlagos","losail","monaco","portimao","imola", "red_bull_ring"]
  podiums=[]

  if driver_lname != "raikkonen":
    for track in circuit:
      request_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/circuits/{track}/results.json"
      response = requests.get(request_url)
      parsed_response = json.loads(response.text)
      result = parsed_response['MRData']['RaceTable']['Races'][0]["Results"][0]["position"]
      if result == "1":
        podiums.append(result)
      if result == "2":
        podiums.append(result)
      if result == "3":
        podiums.append(result)
  else:
    for track in circuitraikkonen:
      request_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/circuits/{track}/results.json"
      response = requests.get(request_url)
      parsed_response = json.loads(response.text)
      result = parsed_response['MRData']['RaceTable']['Races'][0]["Results"][0]["position"]
      if result == "1":
        podiums.append(result)
      if result == "2":
        podiums.append(result)
      if result == "3":
        podiums.append(result)

  resultpodium = {"First place: ":podiums.count("1"), "Second place: ":podiums.count("2"), "Third place: ":podiums.count("3")}
  return resultpodium

def fastestlaps(driver_lname):
  """
  Calculates the number of "fastest laps" the driver earned over the course of the season.

  Parameters:
    driver_lname (str): the last name of a driver, like "alonso"

  Returns:
    An integer depicting the number of fastest laps. 

  Invoke like this: fastestlaps("norris")
  Example return value: 1
  """

  results_url = f"http://ergast.com/api/f1/2021/fastest/1/drivers/{driver_lname}/races.json"
  response = requests.get(results_url)
  results_data = json.loads(response.text)

  fastest_lap = []

  for race in results_data['MRData']['RaceTable']['Races']:
    fastest_lap.append(race["season"])
  
  laps = fastest_lap.count("2021")
  return laps

def master_function(driver_lname):
  """
  Gathers all the stats for a driver.

  Parameters:
    driver_lname (str): the last name of a driver, like "alonso"

  Returns:
    all_results (dict): a dictionary of all the driver's stats, with 10-value pairs: {
      "average grid": resultfin["Average Starting Grid"],
      "average finishing": resultfin["Average Finishing Position"],
      "reason DNF": resultDNF
      "first place count": resultpodium["First place: "],
      "second place count": resultpodium["Second place: "],
      "third place count": resultpodium["Third place: "],
      "number of fastest laps": laps
    }
      resultfin["Average Starting Grid"] (int): an integer of the driver's average starting grid position
      resultfin["Average Finishing Position"] (int): an integer of the driver's average finishing position
      resultDNF (list): list of dictionaries that outline the reason for not finishing a race + how many occurances 
      resultpodium["First place: "] (int): an integer corresponding the the total number of times a driver got first place
      resultpodium["Second place: "] (int): an integer corresponding to the total number of times a driver got second place
      resultpodium["Third place: "] (int): an integer corresponding to the total number of times a driver got third place
      laps (int): an integer count of the number of times a driver has had the fastest lap in the 2021 season

  Invoke like this: master_function("alonso")
  Example return value: {
        "average grid": 10,
        "average finishing": 10,
        "reason DNF": [{'statusId': '1', 'count': '17', 'status': 'Finished'}, {'statusId': '4', 'count': '2', 'status': 'Collision'}, {'statusId': '12', 'count': '1', 'status': '+2 Laps'}, {'statusId': '61', 'count': '1', 'status': 'Wheel nut'}, {'statusId': '137', 'count': '1', 'status': 'Damage'}]
        "first place count": 0,
        "second place count": 0,
        "third place count": 1,
        "number of fastest laps: 4,
  }
  """
  resultfin= average_finish(driver_lname)
  resultDNF= reason_DNF(driver_lname)
  resultpodium= podium_result(driver_lname)
  laps = fastestlaps(driver_lname)

  all_results = {"average grid": resultfin["Average Starting Grid"],
                  "average finishing": resultfin["Average Finishing Position"],
                  "reason DNF":resultDNF,
                  "first place count": resultpodium["First place: "],
                  "second place count": resultpodium["Second place: "],
                  "third place count": resultpodium["Third place: "],
                  "number of fastest laps": laps
  }

  return all_results

def driverinfolist(driver_lname):
  thatlist = {'hamilton': {'name': 'Lewis Hamilton', 'image':'https://images2.minutemediacdn.com/image/fetch/w_736,h_485,c_fill,g_auto,f_auto/https%3A%2F%2Fbeyondtheflag.com%2Fwp-content%2Fuploads%2Fgetty-images%2F2021%2F01%2F1285791902-850x560.jpeg'},
                'bottas': {'name':'Valterri Bottas', 'image':'https://www.formula1.com/content/dam/fom-website/sutton/2020/Styria/Sunday/1255748484.jpg'},
                'max_verstappen':{'name':'Max Verstappen', 'image':'https://img.redbull.com/images/c_limit,w_1500,h_1000,f_auto,q_auto/redbullcom/2021/12/12/uc8q0v9i0m3gpdinfvoe/max-verstappen-abu-dhabi-grand-prix-2021'}, 
                'perez':{'name':'Sergio Perez', 'image':'https://www.grandprix247.com/wp-content/uploads/2021/06/sergio-perez-2021-axerbaijan-grand-prix-winner.jpg'},
                'leclerc':{'name':'Charles Leclerc', 'image':'https://pbs.twimg.com/media/FAESMDvXEAAw_fF?format=jpg&name=large'},
                'sainz':{'name':'Carlos Sainz', 'image':'https://www.grandprix247.com/wp-content/uploads/2021/05/second-place-monaco-carlos-sainz-ferrari-2021.jpg'},
                'norris':{'name':'Lando Norris', 'image':'https://www.goodwood.com/globalassets/.road--racing/event-coverage/mm/2021/10-october/video/f1-2021-russia-pole-lando-norris-mi-goodwood-23102021.jpg'},
                'ricciardo':{'name':'Daniel Ricciardo', 'image':'https://f1i.com/wp-content/uploads/2021/09/XPB_1109696_1200px.jpg'},
                'alonso':{'name':'Fernando Alonso', 'image':'https://d3cm515ijfiu6w.cloudfront.net/wp-content/uploads/2021/03/26131033/Fernando-Alonso-Alpine-PA-copy1.jpg'},
                'ocon':{'name':'Esteban Ocon', 'image':'https://staticg.sportskeeda.com/editor/2021/12/39932-16408526493082-1920.jpg'},
                'gasly':{'name':'Pierre Gasly', 'image':'https://cdn.motorsportmagazine.com/wp-content/uploads/2020/10/28105043/PGPortugal2020.jpg'},
                'tsunoda':{'name':'Yuki Tsunoda', 'image':'https://cdn.motorsportmagazine.com/wp-content/uploads/2021/02/19084632/Tsunoda2.jpg'},
                'vettel':{'name':'Sebastian Vettel', 'image':'https://f1i.com/wp-content/uploads/2021/05/sebastian-vettel-7-e1621790504763.jpg'},
                'stroll':{'name':'Lance Stoll', 'image':'https://cdn-1.motorsport.com/images/amp/YP3J3Ne2/s1000/lance-stroll-aston-martin-1.jpg'},
                'russell':{'name':'George Russell', 'image':'https://cloudfront-us-east-2.images.arcpublishing.com/reuters/FAOFJZETQ5I3TACINNV7CVLPPI.jpg'},
                'latifi':{'name':'Nicholas Latifi', 'image':'https://www.formula1.com/content/dam/fom-website/Upgrade/2021FIAPoolImages/HungarySunday/WILLIAMS_HUNGARY_SUNDAY_01.jpg'},
                'giovinazzi':{'name':'Antonio Giovinazzi', 'image':'https://d3cm515ijfiu6w.cloudfront.net/wp-content/uploads/2021/10/02104137/antonio-giovinazzi-prepares-drive-planetf1.jpg'},
                'raikkonen':{'name':'Kimi Raikkonen', 'image':'https://s3-eu-west-1.amazonaws.com/racingnews-v2-prod/2021/Raikkonen/large-2021-Bahrain-Pre-Season-Test-7.jpg?v=1615649282'},
                'mick_schumacher':{'name':'Mick Schumacher', 'image':'https://f1-insider.com/wp-content/uploads/2021/03/Formel-1-Mick-Schumacher-Haas-2021.jpg'},
                'mazepin':{'name':'Nikita Mazepin', 'image':'https://f1i.com/wp-content/uploads/2021/09/XPB_1111048_1200px-725x500.jpg'}}
  thatguy = thatlist[driver_lname]
  return thatguy

if __name__ == "__main__":
  user_input = input("driver name: ")
  results = master_function(user_input)
  print(results)


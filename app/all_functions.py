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

def avg_pitstop_time(driver_lname):
  """
  Calculates a driver's average pitstop time for the season, rounded to 3 decimal places.

  Parameters:
    driver_lname (str): the last name of a driver, like "alonso"
  
  Returns:
    avg_season_time (float): a float of the driver's average pitstop time 

  Invoke like this: avg_pitstop_time("alonso")
  Example return value: 115.689
  """
  r = 1
  times_per_round = []
  stops_per_round = []

  while r <= total_rounds:

    pit_stop_url = "https://ergast.com/api/f1/2021/" + str(r) + "/drivers/" + driver_lname.lower() + "/pitstops.json"
    response = requests.get(pit_stop_url)
    driver_data = json.loads(response.text)

    if int(driver_data["MRData"]["total"]) > 0:

      num_pitstops = 0
      total_round_time = 0

      for stop in driver_data["MRData"]["RaceTable"]["Races"][0]["PitStops"]:
    
        total_round_time = total_round_time + to_seconds(stop["duration"])
        num_pitstops = num_pitstops + 1
  
      times_per_round.append(total_round_time)
      stops_per_round.append(num_pitstops)
  
    r = r + 1

  avg_season_time = round((sum(times_per_round) / sum(stops_per_round)),3)

  return avg_season_time

def to_seconds(time):
  """
  Converts a string of time into a float of the number of seconds.

  Parameters:
    time (str): a string that corresponds to time, either in the format MM:SS, MM:SS.sss, or SS.sss

  Returns:
    time (float): a float of the number of seconds

  Invoke like this: to_seconds("34:18.58")
  Example return value: 2058.58
  """
  if ":" in time:

    if "." not in time:
      time = time + ".0"

    time = datetime.datetime.strptime(time, "%M:%S.%f")
    minutes = time.minute
    seconds = time.second
    microseconds = time.microsecond
    time = (minutes * 60) + seconds + (microseconds * 0.000001)
  else:
    time = float(time)

  return time

def lap_time_stats(driver_lname):
  """
  Calculates a driver's fastest lap time and average lap time, rounded to 3 decimal places.

  Parameters:
    driver_lname (str): the last name of a driver, like "alonso"

  Returns:
    resultlap (dict): a dictionary containing two key-value pairs: {"Fastest Lap Time": fastest_time, "Average Lap Time": average_time}
      fastest_time (float): a float of the driver's fastest lap time
      average_time (float): a float of the driver's average lap time

  Invoke like this: lap_time_stats("alonso")
  Example return value: {"Fastest Lap Time": 74.389, "Average Lap Time": 115.536}
  """
  results_url = "https://ergast.com/api/f1/2021/drivers/" + driver_lname.lower() + "/results.json"
  response = requests.get(results_url)
  results_data = json.loads(response.text)

  lap_info = []

  for race in results_data["MRData"]["RaceTable"]["Races"]:
    lap_info.append({"round": int(race["round"]), "number of laps": int(race["Results"][0]["laps"])})

  lap_times = []
  lap_number = 1

  for r in lap_info:
    while lap_number < r["number of laps"]:

      lap_url = "http://ergast.com/api/f1/2021/" + str(r["round"]) + "/drivers/" + driver_lname.lower() + "/laps/" + str(lap_number) + ".json"
      response = requests.get(lap_url)
      laps = json.loads(response.text)
      lap_time = laps["MRData"]["RaceTable"]["Races"][0]["Laps"][0]["Timings"][0]["time"]
      lap_times.append(to_seconds(lap_time))
      lap_number = lap_number + 1

  fastest_time = round(min(lap_times),3)
  average_time = round(statistics.mean(lap_times),3)

  resultlap = {"Fastest Lap Time": fastest_time, "Average Lap Time": average_time}

  return resultlap

def master_function(driver_lname):
  """
  Gathers all the stats for a driver.

  Parameters:
    driver_lname (str): the last name of a driver, like "alonso"

  Returns:
    all_results (dict): a dictionary of all the driver's stats, with 10-value pairs: {
      "average grid": resultfin["Average Starting Grid"],
      "average finishing": resultfin["Average Finishing Position"],
      "finishing status": resultDNF["Finishing Status"],
      "count of finishing status": resultDNF["Count"],
      "first place count": resultpodium["First place: "],
      "second place count": resultpodium["Second place: "],
      "third place count": resultpodium["Third place: "],
      "average pitstop": avg_season_time,
      "fastest lap time": resultlap["Fastest Lap Time"],
      "average lap time": resultlap["Average Lap Time"]
    }
      resultfin["Average Starting Grid"] (int): an integer of the driver's average starting grid position
      resultfin["Average Finishing Position"] (int): an integer of the driver's average finishing position
      resultDNF["Finishing Status"] (list): a list of all the driver's finishing statuses
      resultDNF["Count"] (list): a list corresponding the number of times a driver had a certain finishing status
      resultpodium["First place: "] (int): an integer corresponding the the total number of times a driver got first place
      resultpodium["Second place: "] (int): an integer corresponding to the total number of times a driver got second place
      resultpodium["Third place: "] (int): an integer corresponding to the total number of times a driver got third place
      avg_season_time (float): a float of the driver's average pitstop time
      resultlap["Fastest Lap Time"] (float): a float of the driver's fastest lap time
      resultlap["Average Lap Time"] (float): a float of the driver's average lap time

  Invoke like this: master_function("alonso")
  Example return value: {
        "average grid": 10,
        "average finishing": 10,
        "finishing status": ['Finished', '+1 Lap', 'Brakes', 'Rear wing'],
        "count of finishing status": ['11','9','1','1'],
        "first place count": 0,
        "second place count": 0,
        "third place count": 1,
        "average pitstop": 244.165,
        "fastest lap time": 75.026,
        "average lap time": 110.989
  }
  """
  resultfin= average_finish(driver_lname)
  resultDNF= reason_DNF(driver_lname)
  resultpodium= podium_result(driver_lname)
  avg_season_time= avg_pitstop_time(driver_lname)
  resultlap= lap_time_stats(driver_lname)

  all_results = {"average grid": resultfin["Average Starting Grid"],
                  "average finishing": resultfin["Average Finishing Position"],
                  "finishing status": resultDNF["Finishing Status"],
                  "count of finishing status": resultDNF["Count"],
                  "first place count": resultpodium["First place: "],
                  "second place count": resultpodium["Second place: "],
                  "third place count": resultpodium["Third place: "],
                  "average pitstop": avg_season_time,
                  "fastest lap time": resultlap["Fastest Lap Time"],
                  "average lap time": resultlap["Average Lap Time"]
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
                'raikonnen':{'name':'Kimi Raikonnen', 'image':'https://s3-eu-west-1.amazonaws.com/racingnews-v2-prod/2021/Raikkonen/large-2021-Bahrain-Pre-Season-Test-7.jpg?v=1615649282'},
                'mick_schumacher':{'name':'Mick Schumacher', 'image':'https://f1-insider.com/wp-content/uploads/2021/03/Formel-1-Mick-Schumacher-Haas-2021.jpg'},
                'mazepin':{'name':'Nikita Mazepin', 'image':'https://f1i.com/wp-content/uploads/2021/09/XPB_1111048_1200px-725x500.jpg'}}
  thatguy = thatlist[driver_lname]
  return thatguy

if __name__ == "__main__":
  user_input = input("driver name: ")
  results = master_function(user_input)
  print(results)
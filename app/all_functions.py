import requests
import json
import statistics
import datetime

total_rounds = 22 #global variable to hold the number of rounds in the f1 2021 season




def average_finish(driver_lname):
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
  ergast_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/status.json"
  ergast_response = requests.get(ergast_url)
  ergast = json.loads(ergast_response.text)

  #n = 0
  #status = []
  #count = []

  #for line in ergast['MRData']['StatusTable']['Status']:
  #  finish_status = ergast['MRData']['StatusTable']['Status'][n]['status']
  #  status.append(finish_status)
  #  number_finish_status = ergast['MRData']['StatusTable']['Status'][n]['count']
  #  count.append(number_finish_status)
  #  #print(finish_status, number_finish_status)
  #  n = n + 1
#
  #resultDNF = {"Finishing Status": status, "Count": count}

  return ergast['MRData']['StatusTable']['Status']

def podium_result(driver_lname):
  circuit=["yas_marina","jeddah","bahrain","catalunya","istanbul","americas","sochi","monza","zandvoort","spa","hungaroring","silverstone","ricard","BAK","rodriguez","interlagos","losail","monaco","portimao","imola", "red_bull_ring"]

  podiums=[]

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

  resultpodium = {"First place: ":podiums.count("1"), "Second place: ":podiums.count("2"), "Third place: ":podiums.count("3")}
  return resultpodium

def qualifying_time(circuit):
    
  drivers=["bottas","hamilton","max_verstappen","norris","ricciardo","gasly","sainz","leclerc","perez","giovinazzi","vettel","stroll","alonso","ocon","russell","latifi","tsunoda","mick_schumacher","kubica","mazepin"]

  qual_times={}
  for driver in drivers:
      request_url = f"https://ergast.com/api/f1/2021/drivers/{driver}/circuits/{circuit}/qualifying.json"
      response = requests.get(request_url)
      parsed_response = json.loads(response.text)

      times = parsed_response['MRData']['RaceTable']['Races'][0]["QualifyingResults"][0]

      t1= "Q1"
      t2= "Q2"
      t3= "Q3"

      if t1 in times:
        time= parsed_response['MRData']['RaceTable']['Races'][0]["QualifyingResults"][0]["Q1"]
        qual_times[driver]=time
      else:
        pass

      if t2 in times:
        time2= parsed_response['MRData']['RaceTable']['Races'][0]["QualifyingResults"][0]["Q2"]
        qual_times[driver]=time2
      else:
        pass

      if t3 in times:
        time3= parsed_response['MRData']['RaceTable']['Races'][0]["QualifyingResults"][0]["Q3"]
        qual_times[driver]=time3
      else:
        pass

  key_min = min(qual_times.keys(), key=(lambda k: qual_times[k]))
  drivername= min(qual_times, key=qual_times.get)
  drivertime= qual_times[key_min]
  qualdriver= {drivername:drivertime}
  return qualdriver

def avg_pitstop_time(driver_lname):
  """
  Calculates a driver's average pitstop time, either for a single round or the whole season.

  Params:
    driver_lname (str): the last name of a driver, like "alonso"
  
  Returns:
    avg_time (float): a float of the driver's average pitstop time 

  Invoke like this: avg_pitstop_time("alonso")
  """
  round = 1
  times_per_round = []
  stops_per_round = []

  while round <= total_rounds:

    pit_stop_url = "https://ergast.com/api/f1/2021/" + str(round) + "/drivers/" + driver_lname.lower() + "/pitstops.json"
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
  
    round = round + 1

  avg_season_time = sum(times_per_round) / sum(stops_per_round)

  return avg_season_time

def to_seconds(time):
  """
  Converts a string of time into a float of the number of seconds if the format is MM:SS.sss.
  Converts a string of time into a float if the format is SS.sss.

  Parameters:
    time (str): a string that corresponds to time, either in the format MM:SS.sss or SS.sss

  Returns:
    time (float): a float of the number of seconds

  Invoke like this: to_seconds("34:18.580")
  """
  if ":" in time:
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
  Calculates a driver's fastest lap time and average lap time.

  Parameters:
    driver_lname (str): the last name of a driver, like "alonso"

  Returns:
    result (dict): a dictionary containing a driver's fastest lap time and average lap time

  Invoke like this: lap_time_stats("alonso")
  """
  results_url = "https://ergast.com/api/f1/2021/drivers/" + driver_lname.lower() + "/results.json"
  response = requests.get(results_url)
  results_data = json.loads(response.text)

  lap_info = []

  for race in results_data["MRData"]["RaceTable"]["Races"]:
    lap_info.append({"round": int(race["round"]), "number of laps": int(race["Results"][0]["laps"])})

  lap_times = []
  lap_number = 1

  for round in lap_info:
    while lap_number < round["number of laps"]:

      lap_url = "http://ergast.com/api/f1/2021/" + str(round["round"]) + "/drivers/" + driver_lname.lower() + "/laps/" + str(lap_number) + ".json"
      response = requests.get(lap_url)
      laps = json.loads(response.text)
      lap_time = laps["MRData"]["RaceTable"]["Races"][0]["Laps"][0]["Timings"][0]["time"]
      lap_times.append(to_seconds(lap_time))
      lap_number = lap_number + 1

  fastest_time = max(lap_times)
  average_time = statistics.mean(lap_times)

  resultlap = {"Fastest Lap Time": fastest_time, "Average Lap Time": average_time}

  return resultlap

def master_function(driver_lname):
    resultfin= average_finish(driver_lname)
    resultDNF= reason_DNF(driver_lname)
    resultpodium= podium_result(driver_lname)
    avg_season_time= avg_pitstop_time(driver_lname)
    resultlap= lap_time_stats(driver_lname)

    all_results = {"average_finish": resultfin, "reasons_DNF":resultDNF, "podium_results":resultpodium, "avg_pitstop":avg_season_time, "lap_results":resultlap}

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
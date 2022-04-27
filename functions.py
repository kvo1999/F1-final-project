import json
import requests
import datetime

def avg_pitstop_time(racer, option):

  if option.upper() == "R":

    round = input("What round do you want to see data for? ")

    pit_stop_url = "https://ergast.com/api/f1/2021/" + str(round) + "/pitstops.json"
  
    response = requests.get(pit_stop_url)

    pitstop_data = json.loads(response.text)

    for pitstop in pitstop_data["MRData"]["RaceTable"]["Races"][0]["PitStops"]:
      if pitstop["driverId"] == racer:
        avg_time = pitstop["duration"]

  elif option.upper() == "S":
    total_rounds = 23
    round = 1
    stop_counter = 0
    season_pitstop_time = 0

    while round < total_rounds:
      pit_stop_url = "https://ergast.com/api/f1/2021/" + str(round) + "/drivers/" + racer.lower() + "/pitstops.json"
      response = requests.get(pit_stop_url)
      driver_data = json.loads(response.text)

      if int(driver_data["MRData"]["total"]) > 0:
        for stop in driver_data["MRData"]["RaceTable"]["Races"][0]["PitStops"]:
          time = to_seconds(stop["duration"])
          season_pitstop_time = season_pitstop_time + time
          stop_counter = stop_counter + 1
  
      round = round + 1

    avg_time = season_pitstop_time / stop_counter

  return avg_time

def to_seconds(time):
  if ":" in time:
    time = datetime.datetime.strptime(time, "%M:%S.%f")
    minutes = time.minute
    seconds = time.second
    microseconds = time.microsecond
    time = (minutes * 60) + seconds + (microseconds * 0.000001)
  else:
    time = float(time)

  return time
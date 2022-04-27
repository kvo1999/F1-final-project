
import requests
import json


#circuit=["yas_marina","jeddah","bahrain","catalunya","istanbul","americas","sochi","monza","zandvoort","spa","hungaroring","silverstone","red_bull_ring","ricard","BAK","rodriquez","interlagos","losail","monaco","portimao","imola"]
driver_lname= input("Please enter the driver's last name you wish to analyze: ")
circuit= input("which circuit do you wish to analyze?: ")

qual_times=[]

request_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/circuits/{circuit}/qualifying.json"
response = requests.get(request_url)
parsed_response = json.loads(response.text)

times = parsed_response['MRData']['RaceTable']['Races'][0]["QualifyingResults"][0]

t1= "Q1"
t2= "Q2"
t3= "Q3"

if t1 in times:
    time= parsed_response['MRData']['RaceTable']['Races'][0]["QualifyingResults"][0]["Q1"]
    qual_times.append(time)
else:
    pass

if t2 in times:
    time2= parsed_response['MRData']['RaceTable']['Races'][0]["QualifyingResults"][0]["Q2"]
    qual_times.append(time2)
else:
    pass

if t3 in times:
    time3= parsed_response['MRData']['RaceTable']['Races'][0]["QualifyingResults"][0]["Q3"]
    qual_times.append(time3)
else:
    pass

print("fastest qualifying time",min(qual_times))

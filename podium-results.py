import requests
import json


circuit=["yas_marina","jeddah","bahrain","catalunya","istanbul","americas","sochi","monza","zandvoort","spa","hungaroring","silverstone","ricard","BAK","rodriguez","interlagos","losail","monaco","portimao","imola", "red_bull_ring"]
driver_lname= input("Please enter the driver's last name you wish to analyze: ")
#circuit= input("which circuit do you wish to analyze?: ")

podium1=[]
podium2=[]
podium3=[]

for track in circuit:
    request_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/circuits/{track}/results.json"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    result = parsed_response['MRData']['RaceTable']['Races'][0]["Results"][0]["position"]
    if result == "1":
        podium1.append(result)
    if result == "2":
        podium2.append(result)
    if result == "3":
        podium3.append(result)


print(podium1.count("1"), "first place finishes")
print(podium2.count("2"), "second place finishes")
print(podium3.count("3"), "third place finishes")

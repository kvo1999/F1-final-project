import requests
import json


drivers=["bottas","hamilton","max_verstappen","norris","ricciardo","gasly","sainz","leclerc","perez","giovinazzi","vettel","stroll","alonso","ocon","russell","latifi","tsunoda","mick_schumacher","kubica","mazepin"]
circuit= input("which circuit do you wish to analyze?: ")

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
print("Fastest Qualifying Time:", min(qual_times, key=qual_times.get), qual_times[key_min])


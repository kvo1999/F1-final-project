import requests
import json
import statistics

def average_finish(driver_lname):
    ergast_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/results.json"
    ergast_response = requests.get(ergast_url)
    ergast = json.loads(ergast_response.text)
    
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

    print("Average starting grid position:", int(statistics.mean(grid)))
    print("Average finish position:", int(statistics.mean(finish)))


def reason_DNF(driver_lname):
    ergast_url = f"https://ergast.com/api/f1/2021/drivers/{driver_lname}/status.json"
    ergast_response = requests.get(ergast_url)
    ergast = json.loads(ergast_response.text)

    n = 0

    for line in ergast['MRData']['StatusTable']['Status']:
        finish_status = ergast['MRData']['StatusTable']['Status'][n]['status']
        number_finish_status = ergast['MRData']['StatusTable']['Status'][n]['count']
        print(finish_status, number_finish_status)
        n = n + 1


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

    #if podiums.count("1") == 1:
    #    print(podiums.count("1"), "first place finish")
    #elif podiums.count("1")>1 or podiums.count("1")==0:
    #    print(podiums.count("1"), "first place finishes")
    #elif podiums.count("2") == 1:
    #    print(podiums.count("2"), "second place finish")
    #elif podiums.count("2")>1 or podiums.count("2")==0:
    #    print(podiums.count("2"), "second place finishes")
    #elif podiums.count("3") == 1:
    #    print(podiums.count("3"), "third place finish")
    #elif podiums.count("3")>1 or podiums.count("3")==0:
    #    print(podiums.count("3"), "third place finishes")


    print(podiums.count("1"), "first place finishes")
    print(podiums.count("2"), "second place finishes")
    print(podiums.count("3"), "third place finishes")

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
    print("Fastest Qualifying Time:", min(qual_times, key=qual_times.get), qual_times[key_min])


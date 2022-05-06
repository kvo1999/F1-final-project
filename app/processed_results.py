
#processes csv file so data is usable in route 


import csv
import pandas 
import os 

drivers=[]

with open("driverresults.csv") as file_obj:

    reader_obj = csv.reader(file_obj)

    heading= next(file_obj)

    for row in reader_obj:
        drivers.append(row)

def processed_data(driver_lname):
    if driver_lname=="hamilton":
        result = drivers[0]
    elif driver_lname=="bottas":
        result= drivers[1]
    elif driver_lname=="max_verstappen":
        result= drivers[2]
    elif driver_lname=="perez":
        result= drivers[3]
    elif driver_lname=="sainz":
        result= drivers[4]
    elif driver_lname=="norris":
        result= drivers[5]
    elif driver_lname=="leclerc":
        result= drivers[6]
    elif driver_lname=="ricciardo":
        result= drivers[7]
    elif driver_lname=="gasly":
        result= drivers[8]
    elif driver_lname=="alonso":
        result= drivers[9]
    elif driver_lname=="ocon":
        result= drivers[10]
    elif driver_lname=="vettel":
        result= drivers[11]
    elif driver_lname=="stroll":
        result= drivers[12]
    elif driver_lname=="tsunoda":
        result= drivers[13]
    elif driver_lname=="russell":
        result= drivers[14]
    elif driver_lname=="latifi":
        result= drivers[15]
    elif driver_lname=="giovinazzi":
        result= drivers[16]
    elif driver_lname=="mick_schumacher":
        result= drivers[17]
    elif driver_lname=="mazepin":
        result= drivers[18]
    elif driver_lname=="raikonnen":
        result= drivers[19]
    

    return result

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


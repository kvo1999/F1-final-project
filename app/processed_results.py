import csv
import pandas 
import os 

drivers=[]

with open("driverresults.csv") as file_obj:

    reader_obj = csv.reader(file_obj)

    heading= next(file_obj)

    for row in reader_obj:
        drivers.append(row)

#print(drivers)

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







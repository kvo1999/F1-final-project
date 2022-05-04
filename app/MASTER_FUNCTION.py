import requests
import json
import statistics
import datetime

from app.all_functions import reason_DNF
from app.all_functions import podium_result
from app.all_functions import qualifying_time
from app.all_functions import avg_pitstop_time
from app.all_functions import to_seconds
from app.all_functions import lap_time_stats



total_rounds = 22 #global variable to hold the number of rounds in the f1 2021 season

def driver_results(driver_lname):
    average_finish(driver_lname)
    #reason_DNF(driver_lname)
    #podium_result(driver_lname)

    all_results = {"average_finish": resultfin}
    return all_results




#pre runs functions and stores results for each driver in csv file to make processing quicker on web app

from app.all_functions import master_function
from app.all_functions import average_finish
from app.all_functions import reason_DNF
from app.all_functions import podium_result
<<<<<<< Updated upstream
from app.all_functions import avg_pitstop_time
from app.all_functions import lap_time_stats
from app.all_functions import to_seconds
=======
from app.all_functions import fastestlaps
>>>>>>> Stashed changes

import csv

total_rounds = 22
drivers = ["hamilton","bottas","max_verstappen","perez","sainz","norris","leclerc","ricciardo","gasly","alonso","ocon","vettel","stroll","tsunoda","russell","latifi","giovinazzi","mick_schumacher","mazepin","raikkonen"]


for driver in drivers:
    resultfin= average_finish(driver)
    resultDNF= reason_DNF(driver)
    resultpodium= podium_result(driver)
<<<<<<< Updated upstream
    avg_season_time= avg_pitstop_time(driver)
    resultlap= lap_time_stats(driver)
    
    #write results to csv file
    globals()[f"result{driver}"] = [driver, resultfin, resultDNF, resultpodium,avg_season_time,resultlap]


header = ['Driver Name', 'Average Finish', 'Reason for DNF', 'Podium Results', 'Average Pitstop Time', 'Lap Results']
=======
    laps = fastestlaps(driver)
    
    #write results to csv file
    globals()[f"result{driver}"] = [driver, resultfin, resultDNF, resultpodium,laps]


header = ['Driver Name', 'Average Finish', 'Reason for DNF', 'Podium Results', "Fastest Laps"]
>>>>>>> Stashed changes
data= [
    resulthamilton,
    resultbottas,
    resultmax_verstappen,
    resultperez,
    resultsainz,
    resultnorris,
    resultleclerc,
    resultricciardo,
    resultgasly,
    resultalonso,
    resultocon,
    resultvettel,
    resultstroll,
    resulttsunoda,
    resultrussell,
    resultlatifi,
    resultgiovinazzi,
    resultmick_schumacher,
    resultmazepin,
    resultraikkonen
]

with open('driverresults.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)




from app.all_functions import reason_DNF

def test_reason_DNF():
    assert reason_DNF(driver_lname="bottas") == {"Finishing Status": ['Finished', 'Collision', '+2 Laps', 'Wheel nut', 'Damage'], "Count": ['17','2','1','1','1']}
    assert reason_DNF(driver_lname="hamilton") == {"Finishing Status": ['Finished', 'Collision'], "Count": ['21','1']}
    assert reason_DNF(driver_lname="max_verstappen") == {"Finishing Status": ['Finished', 'Accident', 'Collision'], "Count": ['19','1','2']}
    assert reason_DNF(driver_lname="norris") == {"Finishing Status": ['Finished', 'Collision', '+1 Lap'], "Count": ['15','1','6']}
    assert reason_DNF(driver_lname="alonso") == {"Finishing Status": ['Finished', '+1 Lap', 'Brakes', 'Rear wing'], "Count": ['11','9','1','1']}
from app.all_functions import reason_DNF

def test_reason_DNF():
    assert reason_DNF(driver_lname="bottas") == [{'statusId': '1', 'count': '17', 'status': 'Finished'}, {'statusId': '4', 'count': '2', 'status': 'Collision'}, {'statusId': '12', 'count': '1', 'status': '+2 Laps'}, {'statusId': '61', 'count': '1', 'status': 'Wheel nut'}, {'statusId': '137', 'count': '1', 'status': 'Damage'}]
    assert reason_DNF(driver_lname="hamilton") == [{'statusId': '1', 'count': '21', 'status': 'Finished'}, {'statusId': '4', 'count': '1', 'status': 'Collision'}]
    assert reason_DNF(driver_lname="max_verstappen") == [{'statusId': '1', 'count': '19', 'status': 'Finished'}, {'statusId': '3', 'count': '1', 'status': 'Accident'}, {'statusId': '4', 'count': '2', 'status': 'Collision'}]
    assert reason_DNF(driver_lname="norris") == [{'statusId': '1', 'count': '15', 'status': 'Finished'}, {'statusId': '4', 'count': '1', 'status': 'Collision'}, {'statusId': '11', 'count': '6', 'status': '+1 Lap'}]
    assert reason_DNF(driver_lname="alonso") == [{'statusId': '1', 'count': '11', 'status': 'Finished'}, {'statusId': '11', 'count': '9', 'status': '+1 Lap'}, {'statusId': '23', 'count': '1', 'status': 'Brakes'}, {'statusId': '65', 'count': '1', 'status': 'Rear wing'}]
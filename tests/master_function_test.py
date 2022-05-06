from app.all_functions import master_function

def test_master_function():
    assert master_function("alonso") == {
        'average grid': 10, 'average finishing': 10, 'reason DNF': [{'statusId': '1', 'count': '11', 'status': 'Finished'}, {'statusId': '11', 'count': '9', 'status': '+1 Lap'}, {'statusId': '23', 'count': '1', 'status': 'Brakes'}, {'statusId': '65', 'count': '1', 'status': 'Rear wing'}], 'first place count': 0, 'second place count': 0, 'third place count': 1, 'number of fastest laps': 0
  }
    assert master_function("bottas") == {
       'average grid': 6, 'average finishing': 7, 'reason DNF': [{'statusId': '1', 'count': '17', 'status': 'Finished'}, {'statusId': '4', 'count': '2', 'status': 'Collision'}, {'statusId': '12', 'count': '1', 'status': '+2 Laps'}, {'statusId': '61', 'count': '1', 'status': 'Wheel nut'}, {'statusId': '137', 'count': '1', 'status': 'Damage'}], 'first place count': 1, 'second place count': 0, 'third place count': 9, 'number of fastest laps': 4
  }
    
    assert master_function("hamilton") == {
        'average grid': 3, 'average finishing': 3, 'reason DNF': [{'statusId': '1', 'count': '21', 'status': 'Finished'}, {'statusId': '4', 'count': '1', 'status': 'Collision'}], 'first place count': 8, 'second place count': 8, 'third place count': 1, 'number of fastest laps': 6
  }
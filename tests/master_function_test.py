from app.all_functions import master_function

def test_master_function():
    assert master_function("alonso") == {
        "average grid": 10,
        "average finishing": 10,
        "finishing status": ['Finished', '+1 Lap', 'Brakes', 'Rear wing'],
        "count of finishing status": ['11','9','1','1'],
        "first place count": 0,
        "second place count": 0,
        "third place count": 1,
        "average pitstop": 244.165,
        "fastest lap time": 75.026,
        "average lap time": 110.989
  }
    assert master_function("bottas") == {
        "average grid": 6,
        "average finishing": 7,
        "finishing status": ['Finished', 'Collision', '+2 Laps', 'Wheel nut', 'Damage'],
        "count of finishing status": ['17','2','1','1','1'],
        "first place count": 1,
        "second place count": 0,
        "third place count": 9,
        "average pitstop": 180.157,
        "fastest lap time": 69.707,
        "average lap time": 94.819
  }
    
    assert master_function("hamilton") == {
        "average grid": 3,
        "average finishing": 3,
        "finishing status": ['Finished', 'Collision'],
        "count of finishing status": ['21','1'],
        "first place count": 8,
        "second place count": 8,
        "third place count": 1,
        "average pitstop": 214.771,
        "fastest lap time": 72.909,
        "average lap time": 92.733
  }
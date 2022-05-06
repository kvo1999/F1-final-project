from app.all_functions import lap_time_stats

def test_lap_time_stats():
    assert lap_time_stats("alonso") == {"Fastest Lap Time": 75.026, "Average Lap Time": 110.989}
    assert lap_time_stats("bottas") == {"Fastest Lap Time": 69.707, "Average Lap Time": 94.819}
    assert lap_time_stats("hamilton") == {"Fastest Lap Time": 72.909, "Average Lap Time": 92.733}
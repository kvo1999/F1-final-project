from app.all_functions import avg_pitstop_time

def test_avg_pitstop_time():
    assert avg_pitstop_time("alonso") == 244.165
    assert avg_pitstop_time("bottas") == 180.157
    assert avg_pitstop_time("hamilton") == 214.771

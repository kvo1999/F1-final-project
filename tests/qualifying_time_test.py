from app.all_functions import qualifying_time

def test_qualifying_time():
    assert qualifying_time("yas_marina") == {"alonso":"0"}
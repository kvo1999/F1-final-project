from app.all_functions import to_seconds

def test_to_seconds ():
    assert to_seconds("120.67") == 120.67
    assert to_seconds("55.3657") == 55.3657
    assert to_seconds("35:45") == 2145
    assert to_seconds("20:30.36") == 1230.36

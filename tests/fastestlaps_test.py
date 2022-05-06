from app.all_functions import fastestlaps

def test_fastestlap_result():
    assert fastestlaps("alonso") == 0
    assert fastestlaps("hamilton") == 6
    assert fastestlaps("bottas") == 4


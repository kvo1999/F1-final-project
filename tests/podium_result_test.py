from app.all_functions import podium_result

#circuit=["yas_marina","jeddah","bahrain","catalunya","istanbul","americas","sochi","monza","zandvoort","spa","hungaroring","silverstone","ricard","BAK","rodriguez","interlagos","losail","monaco","portimao","imola", "red_bull_ring"]


def test_podium_result():
    assert podium_result("yas_marina") == {"First place: ":5, "Second place: ":0, "Third place: ":8}

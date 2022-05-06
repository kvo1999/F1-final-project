from app.all_functions import podium_result

def test_podium_result():
    assert podium_result("alonso") == {"First place: ":0, "Second place: ":0, "Third place: ":1}
    assert podium_result("bottas") == {"First place: ":1, "Second place: ":0, "Third place: ":9}
    assert podium_result("hamilton") == {"First place: ":8, "Second place: ":8, "Third place: ":1}
    assert podium_result("raikkonen") == {"First place: ":0, "Second place: ":0, "Third place: ":0}
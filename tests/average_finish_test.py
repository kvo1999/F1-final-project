from app.all_functions import average_finish

#drivers=["bottas","hamilton","max_verstappen","norris","ricciardo","gasly","sainz"
#,"leclerc","perez","giovinazzi","vettel","stroll","alonso","ocon","russell",
#"latifi","tsunoda","mick_schumacher","kubica","mazepin"]


def test_average_finish():
    assert average_finish(driver_lname="bottas") == {"Average Starting Grid": 6, "Average Finishing Position": 7}
    assert average_finish(driver_lname="hamilton") == {"Average Starting Grid": 3, "Average Finishing Position": 3}
    assert average_finish(driver_lname="max_verstappen") == {"Average Starting Grid": 3, "Average Finishing Position": 4}
    assert average_finish(driver_lname="norris") == {"Average Starting Grid": 7, "Average Finishing Position": 7}
    assert average_finish(driver_lname="ricciardo") == {"Average Starting Grid": 10, "Average Finishing Position": 9}
    assert average_finish(driver_lname="gasly") == {"Average Starting Grid": 6, "Average Finishing Position": 9}
    assert average_finish(driver_lname="sainz") == {"Average Starting Grid": 8, "Average Finishing Position": 6}
    assert average_finish(driver_lname="alonso") == {"Average Starting Grid": 10, "Average Finishing Position": 10}
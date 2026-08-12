from cfd_monitor import Room
import pytest


def test_update_temp():
    test_room = Room("testroom", 28, 40)

    test_room.update_temp(30)

    assert test_room.temp == 30


def test_fahrenheit():
    new_room = Room("new_room", 28, 35)

    assert new_room.to_fahrenheit() == 82.4


# made single function for checking humidity levels irrespective of how many object we create it checks temp and give the message
@pytest.mark.parametrize(  # used decorator to change behaviour of tes chcek humidity test method which asks twwo parameters
    "humidity, expected_msg",
    [
        (24, "Humidity levels are normal"),
        (100, "Warning: Environment is too humid!"),
    ],
)
def test_check_humidity(humidity, expected_msg):
    new = Room("new", 24, humidity)
    assert new.check_humidity() == expected_msg

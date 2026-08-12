from cfd_monitor import Room
import pytest


def test_update_temp():
    test_room = Room("testroom", 28, 40)

    test_room.update_temp(30)

    assert test_room.temp == 30


def test_fahrenheit():
    new_room = Room("new_room", 28, 35)

    assert new_room.to_fahrenheit() == 82.4


@pytest.mark.parametrize(
    "humidity, expected_msg",
    [
        (24, "Humidity levels are normal."),
        (100, "Warning: Environment is too humid!"),
    ],
)
def test_check_humidity(humidity, expected_msg):
    new = Room("new", 24, humidity)

    assert new.check_humidity() == expected_msg

from cfd_monitor import Room


def test_update_temp():
    test_room = Room("testroom", 28)
    test_room.update_temp(30)
    assert test_room.temp == 30

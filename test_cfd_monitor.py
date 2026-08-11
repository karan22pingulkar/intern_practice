from cfd_monitor import Room


# update temp test function
def test_update_temp():
    test_room = Room("testroom", 28, 40)
    test_room.update_temp(30)
    assert test_room.temp == 30


# humidity check func
def test_check_humidity():
    server = Room("server_room", 24, 100)
    server.check_humidity()
    assert server.check_humidity() == "Warning: Environment is too humid!"

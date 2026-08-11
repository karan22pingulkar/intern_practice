from cfd_monitor import Room


# checking if the updated temp is working correct
def test_update_temp():
    test_room = Room("testroom", 28, 40)
    test_room.update_temp(30)
    assert test_room.temp == 30


def test_check_humidity():  # humidity check func
    server = Room("server_room", 24, 100)
    server.check_humidity()
    assert server.check_humidity() == "Warning: Environment is too humid!"

    print(f"{server}\n{server.check_humidity()}")


def test_fahrenheit():
    new_room = Room("new_room", 28, 35)
    new_room.to_fahrenheit()
    # 28 C is 82.4 in Fahrenheit
    assert new_room.to_fahrenheit() == 82.4

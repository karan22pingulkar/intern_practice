def test_check_humidity():
    server = Room("server_room", 24, 100)
    server.check_humidity()
    assert server.check_humidity == "Warning: Environment is too humid!"

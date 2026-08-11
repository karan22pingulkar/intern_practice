class Room:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp

    def update_temp(self, new_temp):
        self.temp = new_temp


# lab = Room("server_room", 24)
# print(lab.temp)

# lab.update_temp(24.5)

# print(lab.temp)

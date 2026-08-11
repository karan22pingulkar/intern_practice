class Room:
    def __init__(self, name, temp, humidity):
        self.name = name
        self.temp = temp
        self.humidity = humidity

    def update_temp(self, new_temp):
        self.temp = new_temp

    def __str__(self):
        return (
            f"Room name: {self.name}, Temp: {self.temp}°C, Humidity: {self.humidity}%"
        )

    def check_humidity(self):
        if self.humidity > 90:
            message = "Warning: Environment is too humid!"
        else:
            message = "Humidity levels are normal."

        return message

    def to_fahrenheit(self):
        return (self.temp * 9 / 5) + 32


# server = Room("server", 34, 910)
# print(f"{server}\n{server.check_humidity()}")

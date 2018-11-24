from Actuation.IVehicleActuator import IVehicleActuator


class StrawsAndPopsicleSticks(IVehicleActuator):

    def __init__(self):
        self.speed = 0
        self.turning_speed = 0

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, val: float):
        self._speed = val
        # and now actually set it on the GPIO pins

    @property
    def turning_speed(self) -> float:
        return self._turning_speed

    @turning_speed.setter
    def turning_speed(self, val: float):
        self._turning_speed = val
        # and now actually set it on the GPIO pins

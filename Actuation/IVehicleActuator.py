from abc import ABC, abstractmethod


class IVehicleActuator(ABC):

    _speed: float
    _turning_speed: float

    @property
    @abstractmethod
    def speed(self) -> float:
        """gets the current speed of the vehicle in metres per second (-ve is backwards)"""
        return self._speed

    @speed.setter
    @abstractmethod
    def speed(self, val: float):
        """sets the speed in metres per second (-ve is backwards) and
        makes the vehicle also physically reflect this change"""
        self._speed = val

    @property
    @abstractmethod
    def turning_speed(self) -> float:
        """gets the turning speed in degrees per second (+ve is right, -ve is left)"""
        return self._turning_speed

    @turning_speed.setter
    @abstractmethod
    def turning_speed(self, val: float):
        """sets the turning speed in degrees per second (+ve is right, -ve is left) and
        makes the vehicle also physically reflect this change"""
        self._turning_speed = val

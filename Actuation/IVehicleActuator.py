from abc import ABC, abstractmethod


class IVehicleActuator(ABC):

    _speed: float
    _turning_speed: float

    @property
    @abstractmethod
    def speed(self) -> float:
        """gets the current speed of the vehicle in metres per second (-ve is backwards)"""
        pass

    @speed.setter
    @abstractmethod
    def speed(self, val: float):
        """sets the speed in metres per second (-ve is backwards) and
        makes the vehicle also physically reflect this change"""
        pass

    @property
    @abstractmethod
    def turning_speed(self) -> float:
        """gets the turning speed in degrees per second (+ve is right, -ve is left)"""
        pass

    @turning_speed.setter
    @abstractmethod
    def turning_speed(self, val: float):
        """sets the turning speed in degrees per second (+ve is right, -ve is left) and
        makes the vehicle also physically reflect this change"""
        pass

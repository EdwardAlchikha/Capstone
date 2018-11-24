from abc import ABC, abstractmethod

from Actuation.IVehicleActuator import IVehicleActuator
from Vision.ICamera import ICamera


class IDecisionMaker(ABC):

    _vehicle_actuator: IVehicleActuator
    _camera: ICamera

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

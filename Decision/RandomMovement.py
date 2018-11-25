from random import random

from Actuation.IVehicleActuator import IVehicleActuator
from Decision.IDecisionMaker import IDecisionMaker
from Vision.ICamera import ICamera


class RandomMovement(IDecisionMaker):

    def __init__(self, vehicle_actuator: IVehicleActuator, camera: ICamera):
        self._vehicle_actuator = vehicle_actuator
        self._camera = camera

    def start(self):
        self._vehicle_actuator.speed = random() * 0.5
        self._vehicle_actuator.turning_speed = random() * 15
        print(str(self._vehicle_actuator.speed) + " " + str(self._vehicle_actuator.turning_speed) + "\n")

    def stop(self):
        self._vehicle_actuator.speed = 0
        self._vehicle_actuator.turning_speed = 0
        print(str(self._vehicle_actuator.speed) + " " + str(self._vehicle_actuator.turning_speed) + "\n")

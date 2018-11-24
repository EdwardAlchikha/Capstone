from random import random

from Actuation.StrawsAndPopsicleSticks import StrawsAndPopsicleSticks
from Decision.IDecisionMaker import IDecisionMaker
from Vision.DoesNothingCamera import DoesNothingCamera


class RandomMovement(IDecisionMaker):

    def __init__(self):
        self._vehicle_actuator = StrawsAndPopsicleSticks()
        self._camera = DoesNothingCamera()

    def start(self):
        self._vehicle_actuator.speed = random() * 0.5
        self._vehicle_actuator.turning_speed = random() * 15
        print(str(self._vehicle_actuator.speed) + " " + str(self._vehicle_actuator.turning_speed) + "\n")

    def stop(self):
        self._vehicle_actuator.speed = 0
        self._vehicle_actuator.turning_speed = 0
        print(str(self._vehicle_actuator.speed) + " " + str(self._vehicle_actuator.turning_speed) + "\n")

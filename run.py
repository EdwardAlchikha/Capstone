from time import sleep

from Actuation.StrawsAndPopsicleSticks import StrawsAndPopsicleSticks
from Decision.RandomMovement import RandomMovement
from Vision.DoesNothingCamera import DoesNothingCamera

if __name__ == '__main__':
    camera = DoesNothingCamera()
    vehicle_actuator = StrawsAndPopsicleSticks()
    decision_maker = RandomMovement(vehicle_actuator, camera)
    decision_maker.start()
    sleep(10)
    decision_maker.stop()

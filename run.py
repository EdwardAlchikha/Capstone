from time import sleep

from Decision.RandomMovement import RandomMovement

if __name__ == '__main__':
    decision_maker = RandomMovement()
    decision_maker.start()
    sleep(10)
    decision_maker.stop()

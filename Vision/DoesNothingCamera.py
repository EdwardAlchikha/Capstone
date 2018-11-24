from Vision.ICamera import ICamera


class DoesNothingCamera(ICamera):

    def __init__(self):
        print("I do nothing!\n")

    def placeholder(self):
        print("I do nothing!")

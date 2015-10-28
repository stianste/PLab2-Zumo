from time import sleep
from ultrasonic import *
from Arbitrator import Arbitrator
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from derp import Derp
from motors import Motors
from driveToColor import driveToColor
from watchOutForTheWall import WatchOutForTheWall

class BBCON():

    def __init__(self, behaviors, sensobs):
        #init instance variables from input.
        self.behaviors = set(behaviors)
        self.sensobs = sensobs # Dictionary of sensobject, 'camera' -> camera sensobj
        self.arbitrator = Arbitrator()
        self.motors = Motors()
       

    def _update_sensobs(self):
          for ob in self.sensobs:
              self.sensobs[ob].update()

    def _update_behaviors(self):
        for behavior in self.behaviors:
            mr = behavior.get_update() # this also toggels the active_flag for the behavior
            if behavior.active_flag:
                self.arbitrator.add_mr(mr)

    def loop(self):
      self._update_sensobs()
      self._update_behaviors()
      mr = self.arbitrator.choose_action()
      self.motors.do(mr.action)
      sleep(0.01)


rs = ReflectanceSensors()
camera = Camera()
ultra = Ultrasonic()
sensobs = {'ir' : rs, 'camera': camera, 'ultrasonic' : ultra }

# behaviors = [Derp(8), driveToColor(sensobs, 10), WatchOutForTheWall(sensobs, 10)]
behaviors = [WatchOutForTheWall(sensobs, 10)]

bbcon = BBCON(behaviors, sensobs)
bbcon.motors.setMax(400);
print("max speed:" + str(bbcon.motors.max));

while True:
  bbcon.loop()

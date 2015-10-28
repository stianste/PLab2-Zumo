from time import sleep
from ultrasonic import *
from Arbitrator import Arbitrator
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from derp import Derp
from motors import Motors
from driveToColor import driveToColor
from watchOutForTheWall import WatchOutForTheWall
from turnAtEdge import TurnAtEdge
from zumo_button import ZumoButton

class BBCON():

    def __init__(self, behaviors, sensobs):
        #init instance variables from input.
        self.behaviors = set(behaviors)
        self.sensobs = sensobs # Dictionary of sensobject, 'camera' -> camera sensobj
        self.camera_count = 0
        self.arbitrator = Arbitrator()
        self.motors = Motors()
       

    def _update_sensobs(self):
          self.camera_count += 1
          self.camera_count = self.camera_count % 10
          for ob in self.sensobs:
              if ob != 'camera':
                self.sensobs[ob].update()
              elif self.camera_count == 0:
                self.motors.stop()
                self.camera_count = 0
                self.sensobs[ob].update()


    def _update_behaviors(self):
        for behavior in self.behaviors:
          if behavior.__class__ != 'driveToColor':
            print('No camera', self.camera_count)
            mr = behavior.get_update() # this also toggels the active_flag for the behavior
            if behavior.active_flag:
                self.arbitrator.add_mr(mr)
          elif self.camera_count == 0:
            print('CAMERA EVAL')
            mr = behavior.get_update()
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
behaviors = [];

#behaviors.append(WatchOutForTheWall(sensobs, 1));

behaviors.append(driveToColor(sensobs, 10))

bbcon = BBCON(behaviors, sensobs)

bbcon.motors.setMax(200);
bbcon.motors.setTurnSpeed(500);
bbcon.motors.setTurnDur(10); #bør være rundt 12

print("max speed:" + str(bbcon.motors.max));
button = ZumoButton();
button.wait_for_press();
sleep(2);
while True and button.button_pressed():
  bbcon.loop()

bbcon.motors.stop();

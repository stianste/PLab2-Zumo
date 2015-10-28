from Behavior import Behavior
from motor_rec import Motor_Rec
from ultrasonic import *


class WatchOutForTheWall(Behavior):
  def __init__(self, sensobs, static_pri):
    super().__init__(sensobs, True, static_pri)

  def get_update(self):
    action = 0.25;
    score=10;
    distance = self.sensobs['ultrasonic'].get_value()
    print("distance: " + str(distance));

    if(distance<20 and distance>0):
      degrees = 180 - 9*distance;
      action = ["r",degrees];
      print("sving: " + str(degrees) );
    
    else:
      action = 1;
    return Motor_Rec(10, action)

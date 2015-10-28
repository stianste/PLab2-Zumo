from Behavior import Behavior
from motor_rec import Motor_Rec
from ultrasonic import *


class WatchOutForTheWall(Behavior):
  def __init__(self, sensobs, static_pri):
    super().__init__(sensobs, True, static_pri)
	
	
  def get_update(self):
    action = 0.25;
    score=10;
    values = self.sensobs['ultrasonic'].get_value()
    print("distance: " + str(distance));

    if(distance<10 and distance>0):
		action = ["r",45];
    elif distance<15 and distance>0:
      action = 0;
    elif(distance<40 and distance>0):
      action = (distance/60)
    else:
      action = 1;
    return Motor_Rec(10, action)

from Behavior import Behavior
from motor_rec import Motor_Rec
from ultrasonic import *


class WatchOutForTheWall(Behavior):
  def __init__(self, sensobs, static_pri):
    super().__init__(sensobs, True, static_pri)

  def get_update(self):
    speed_value = 1;
    turn_value = 0.0;
    score=10;
    distance = self.sensobs['ultrasonic'].get_value()
    print("distance: " + str(distance));

    if(distance<10 and distance>0):
      speed_value = -(5/distance);
    elif distance<15 and distance>0:
      speed_value = 0;
    elif(distance<40 and distance>0):
      speed_value =(float((distance)/30)); 
    return Motor_Rec(score, turn_value, speed_value, 1)

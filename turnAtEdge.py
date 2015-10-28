from Behavior import Behavior
from motor_rec import Motor_Rec
from reflectance_sensors import *

class TurnAtEdge():
	def __init__(self, sensobs, static_pri):
		super().__init__(sensobs, True, static_pri)
	
	def get_update(self):
    speed_value = 0.25;
    turn_value = 0.0;
    score=10;
    values = self.sensobs['ir'].get_value()
    print("distance: " + str(values));

    
    return Motor_Rec(10, 0, speed_value, 2)
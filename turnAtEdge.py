from Behavior import Behavior
from motor_rec import Motor_Rec
from reflectance_sensors import *

class TurnAtEdge(Behavior):
    threshold = 0.3
    pri = 10
    def __init__(self, sensobs):
            super().__init__(sensobs, True, pri)
            self.ir = sensobs['ir'].get_value()
    def _update_flag(self):
        #Checks the urrent values of the ir sensor and checks if any of them are darker than threshold
        values = self.ir.get_value
        for v in values:
            if v < threshold:
                self.active_flag = True
                return True
        return False
        
    def _sense_and_act(self):
        speed_value = 0.25;
        turn_value = 0.0;
        score=10;
        values = self.sensobs['ir'].get_value()
        #print("distance: " + str(values));
        if self.active_flag:
            self.match_degree = 200
            self.motor_recommendation.action = ['l', 90] 

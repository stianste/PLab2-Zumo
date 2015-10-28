
from motor_rec import Motor_Rec

class Arbitrator():
    def __init__(self):
        self.forward_rec = Motor_Rec(1,1);
        self.motor_recs = [self.forward_rec] #instansiates a min queue of motor_recommendations
        

    def add_mr(self, motor_rec):

        self.motor_recs.append(motor_rec)

    def choose_action(self):
        #gets the motor_rec with highest priority, returns it and empties the queueue 
        
        val = max(self.motor_recs)
        print(val.__class__)
        self.motor_recs = [self.forward_rec];
        return val
